import random

from fastapi import Depends
from src.repositories.sqlalchemy_repo import SQLAlchemyRepository
from src.services.abstract_srv import AbstractService


class InferenceSrv(AbstractService):
    _repository: SQLAlchemyRepository

    def __init__(self, repo: SQLAlchemyRepository = Depends(SQLAlchemyRepository)):
        super().__init__(repo)

    async def preprocess_data(self, data):
        # TODO
        return data

    async def predict(self, data):
        # TODO
        data = await self.preprocess_data(data)
        return random.randint(1000, 50000)
