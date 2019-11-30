import abc


class PredictionScorer(abc.ABC):
    @abc.abstractmethod
    async def score_prediction(self, df_predict):
        pass
