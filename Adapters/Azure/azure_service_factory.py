from Common.Contracts import ServiceFactory, QueueService, TableStorage
from .Config import AzureConfig
from . import AzureCosmosDb, AzureStorageQueue, AzureResourceService, AzureResourceServiceConfig

class AzureServiceFactory(ServiceFactory):
    def __init__(self, config:AzureConfig):
        self._config = config

    def table_storage(self):
        return AzureCosmosDb(self._config.get_cosmos_storage_config())

    def queue(self, name):
        return AzureStorageQueue(
            self._config.get_queue_name(),
            self._config.get_storage_config())
    
    def resource_service(self, subscription_id):
        return AzureResourceService(self._config.get_resource_config(subscription_id))