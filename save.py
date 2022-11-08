import json
from datetime import datetime
from Enumeration import SaveData

class Save():
    def __init__(self):
        self.file_name = "config.json"
        self.data = {
            'server_address' : "" ,
            'password' : '' ,
            'user' : '' ,
            'port' : 6
        }
        self.restore_data()
        
    def save_data(self):
        self.data['last run'] =str(datetime.now())
        with open(self.file_name, 'w') as file:

            json.dump(self.data, file)  
    def restore_data(self):
        try:
            with open(self.file_name) as file:
                self.data = json.load(file)
        except Exception as e:
            pass
            print(e)
    def get_data(self, data: SaveData):
        if data == SaveData.SERVER_ADDRESS:
            return self.data['server_address']
        elif data == SaveData.PASSWORD:
            return self.data['password']
        elif data == SaveData.PORT:
            return self.data['port']
        elif data == SaveData.USER:
            return self.data['user']
        