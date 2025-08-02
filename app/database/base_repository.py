from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional


T = TypeVar('T')


class BaseRepository(ABC, Generic[T]):

    def __init__(self, session):
        self.session = session


    @abstractmethod
    async def create(
        self, 
        entity: T
    ) -> T:

        raise NotImplementedError


    @abstractmethod
    async def read(
        self, 
        id: int
    ) -> Optional[T]:

        raise NotImplementedError


    @abstractmethod
    async def update(
        self, 
        entity: T
    ) -> T:

        raise NotImplementedError


    @abstractmethod
    async def delete(
        self, 
        id: int
    ) -> None:

        raise NotImplementedError
    