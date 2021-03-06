from abc import ABC, abstractmethod
from . import ResourceService

class ServiceFactory(ABC):

    @abstractmethod
    def table_storage(self):
        raise NotImplementedError("table_storage is not implemented")

    @abstractmethod
    def queue(self, name):
        raise NotImplementedError("queue is not implemented")
    
    @abstractmethod
    def resource_service(self, subscription_id) -> ResourceService:
        raise NotImplementedError("resource_service is not implemented")

