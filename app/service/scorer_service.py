from datetime import datetime
import io
import pandas as pd

from models import SubmissionResponse
from scorer_interface import PredictionScorer


class ScorerService:

    def __init__(self,
                 prediction_scorer: PredictionScorer = None,
                 scores_table=None,
                 database=None):

        if prediction_scorer is None:
            from app import PredictionScorerImpl
            self._prediction_scorer = PredictionScorerImpl()
        else:
            self._prediction_scorer = prediction_scorer

        if scores_table is None:
            from db.scoresdb import scores as injected_scores
            self._scores_table = injected_scores
        else:
            self._scores_table = scores_table

        if database is None:
            from db.db import database as injected_database
            self._database = injected_database

    async def handle_submission(self, file_stream, user_id):
        try:
            df = pd.read_csv(io.BytesIO(await file_stream.read()))
            score = await self._prediction_scorer.score_prediction(df)

            insert_score_query = self._scores_table.insert().values(user_id=user_id,
                                                                    score=score,
                                                                    submission_time=datetime.utcnow())
            await self._database.execute(insert_score_query)

            return SubmissionResponse(success=True, score=score, message="Score submitted")

        except UnicodeDecodeError:

            return SubmissionResponse(success=False, score=-1, message="Uploaded file isn't valid.")
        except Exception as e:
            return SubmissionResponse(success=False, score=-1, message=e.msg)
