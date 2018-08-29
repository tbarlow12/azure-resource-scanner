from azure.common.credentials import ServicePrincipalCredentials, BasicTokenAuthentication

class AzureStorageConfig:
    def __init__(self, accountName, accountKey):
        self.account_name = accountName
        self.account_key = accountKey