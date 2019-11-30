from fastapi import FastAPI
from controllers.users import app as user_controller
from controllers.score import app as score_controller
import uvicorn

from db.db import database

app = FastAPI()
app.include_router(user_controller, prefix='/user')
app.include_router(score_controller, prefix='/score')


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
