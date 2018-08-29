from Common.Contracts.subscription_service import SubscriptionService
from azure.mgmt.resource.subscriptions import SubscriptionClient
from .Config import AzureResourceServiceConfig


class AzureSubscriptionService(SubscriptionService):

    def __init__(self, config:AzureResourceServiceConfig):
        self._client = SubscriptionClient(config.CREDENTIALS)

    def get_subscriptions(self):
        return [sub.serialize(True) for sub in self._client.subscriptions.list()]
