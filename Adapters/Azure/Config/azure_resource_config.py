from . import AzureCredentialConfig

class AzureResourceServiceConfig:
    def __init__(self, subscriptionId, creds:AzureCredentialConfig):
        self.CREDENTIALS = creds.get_credentials()
        self.SUBSCRIPTION_ID = subscriptionId