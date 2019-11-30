from models import RegisterUserResponse, LoginResponse
from datetime import datetime


class UserService:

    def __init__(self,
                 security_service=None,
                 users_table=None,
                 database=None):

        if security_service is None:
            from di import security_service
            self._security_service = security_service
        else:
            self._security_service = security_service

        if users_table is None:
            from db.usersdb import users as injected_users
            self._users_table = injected_users
        else:
            self._users_table = users_table

        if database is None:
            from db.db import database as injected_database
            self._database = injected_database

    async def create_new_user(self, user_name, password):
        select_user_exists_query = self._users_table.select(self._users_table).where(
            self._users_table.c.user_name == user_name)
        create_user_query = self._users_table.insert() \
            .values(user_name=user_name,
                    password_hash=self._security_service.encrypt_password(password),
                    created_on=datetime.utcnow())

        if len(await self._database.fetch_all(select_user_exists_query)) == 0:
            await self._database.execute(create_user_query)
            return RegisterUserResponse(success=True, message=f"User: {user_name} created")
        else:
            return RegisterUserResponse(success=False, message=f"User: {user_name} already exists")

    async def check_login(self, user_name, password):
        select_user_exists_query = self._users_table.select(self._users_table).where(
            self._users_table.c.user_name == user_name)

        response = await self._database.fetch_one(select_user_exists_query)
        success = response is not None and self._security_service.check_encrypted_password(password,
                                                                                           response.password_hash)

        if success:
            update_user_login_time = self._users_table.update(self._users_table).where(
                self._users_table.c.user_id == response.user_id).values(
                last_login=datetime.utcnow())
            await self._database.execute(update_user_login_time)
        return LoginResponse(success=success)
