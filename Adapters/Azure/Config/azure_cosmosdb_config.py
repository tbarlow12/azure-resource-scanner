from .azure_storage_config import AzureStorageConfig

class AzureCosmosDbConfig():
    def __init__(self, tableName, storage:AzureStorageConfig):
        self.account_name = storage.account_name
        self.account_key = storage.account_key
        self.table_name = tableName