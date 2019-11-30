from scorer_interface import PredictionScorer
from service.security_service import SecurityService
from service.scorer_service import ScorerService
from service.user_service import UserService


class PredictionScorerImpl(PredictionScorer):

    async def score_prediction(self, df_predict):
        import random
        return random.uniform(0, 1)


security_service = SecurityService(salt=b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY=')
user_service = UserService()
scorer_service = ScorerService()
