import pymongo

from pymongo.collection import Collection


class Save_dict_mongo:
    def __init__(self):
        # 建立连接
        self.client = pymongo.MongoClient(host='192.168.244.128', port=27017, username='admin', password='JJP123.')
        # client.dbName.authenticate('admin','JJP990308')
        self.db = self.client['https_attack']

    def insert_item(self, item):
        db_collection = Collection(self.db, 'capture_data')
        db_collection.insert_one(item)


mongo_info = Save_dict_mongo()