from cryptography.fernet import Fernet


class SecurityService:
    def __init__(self,
                 salt: bytes = None):
        if salt is None:
            import os
            self._cipher_suite = Fernet(str.encode(os.environ['ML_SALT_KEY']))
        else:
            self._cipher_suite = Fernet(salt)

    def encrypt_password(self, password):
        return self._cipher_suite.encrypt(str.encode(password))

    def check_encrypted_password(self, password, hashed):
        return password == self._cipher_suite.decrypt(hashed).decode()
