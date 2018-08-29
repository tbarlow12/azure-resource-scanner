from abc import ABC, abstractmethod

class SubscriptionService(ABC):

    @abstractmethod
    def get_subscriptions(self):
        raise NotImplementedError("get_subscriptions is not implemented")
