import abc

from app.dto.create_transport import CreateTransport
from app.dto.transport import Transport
from app.dto.update_transport import UpdateTransport


class TransportsRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    async def create_transport(self, create_dto: CreateTransport) -> Transport:
        ...

    @abc.abstractmethod
    async def update_transport(self, transport_id: int, update_dto: UpdateTransport) -> Transport:
        ...

    @abc.abstractmethod
    async def get_transports(self) -> list[Transport]:
        ...
