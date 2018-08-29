import json
import azure.functions
import logging
from Adapters.Azure import AzureConfig,AzureServiceFactory
from Common import ResourceScanner, Config
from Common.Contracts import Queue

class LoggingQueue(Queue):
    def push(self, message):
        logging.info(message)

    def pop(self):
        raise NotImplementedError("Should have implemented pop")

    def peek(self):
        raise NotImplementedError("Should have implemented peek")

def test_scanner():
    data = {
        "subscriptionId" : "808b8977-950a-4a96-8229-b48d708aa455",
        "typeName" : "storage"
    }
    config = Config()
    azureConfig = AzureConfig(config)
    factory = AzureServiceFactory(azureConfig)
    ResourceScanner(factory, LoggingQueue()).execute(data)
