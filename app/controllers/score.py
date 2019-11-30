from fastapi import APIRouter, UploadFile, File

from di import scorer_service
from models import SubmissionResponse


app = APIRouter()


@app.post("/submit/", response_model=SubmissionResponse)
async def submit_score(file: UploadFile = File(...)):
    return await scorer_service.handle_submission(file, 1)  # TODO read user from cookie


@app.get("/scoreboard/")
async def score_board():
    return "TODO"
