import json
import uuid

from azure.cosmosdb.table.tableservice import TableService
from Common.Contracts import TableStorage
from .Config import AzureCosmosDbConfig

class AzureCosmosDb(TableStorage):

    def __init__(self, config:AzureCosmosDbConfig):
        self._tableService = TableService(account_name=config.account_name, account_key=config.account_key)
        self._tableName = config.table_name

    def prepare_entry_for_insert(self, json_entry):

        # using location as the partition key. This will keep all the data from
        # the same location on the same node for fastest access
        location = json_entry['location']
        json_entry['PartitionKey'] = location
        json_entry['RowKey'] = str(uuid.uuid3(uuid.NAMESPACE_DNS, json_entry['id']))
        data_to_write = json.dumps(json_entry)
        dict = json.loads(data_to_write)

        # cosmos does not allow for an entry with key 'id'
        modified_data = {}
        for key, value in dict.items():
            if key == 'id':
                modified_data['resourceid'] = str(value)
            else:
                modified_data[key] = str(value)

        return modified_data

    
    def check_entry_exists(self, entry):
        try:
            self.query(entry['PartitionKey'], entry['RowKey'])
            return True
        except:
            return False

    def write(self, entry):
        prepared = self.prepare_entry_for_insert(entry)

        if not self.check_entry_exists(prepared):
            self._tableService.insert_entity(self._tableName, prepared)
        else:
            self._tableService.update_entity(self._tableName, prepared)

    def query(self, partitionkey, rowkey):
        task = self._tableService.get_entity(self._tableName, partitionkey, rowkey)
        return task

    def delete(self, partitionkey, rowkey):
        self._tableService.delete_entity(self._tableName, partitionkey, rowkey)
