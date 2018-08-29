from azure.common.credentials import ServicePrincipalCredentials, BasicTokenAuthentication

class AzureCredentialConfig:
    def __init__(self, clientId, tenant, secret):
        self.clientId = clientId
        self.secret = secret
        self.tenant = tenant
    
    def get_credentials(self):
        return ServicePrincipalCredentials(
            self.clientId,
            self.secret,
            tenant=self.tenant)
