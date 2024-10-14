import json
import os
from datetime import datetime


class Database:
    def __init__(self, filename='database.json'):
        self.filename = filename
        self.database = {}
        self.load_database()

    def load_database(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.database = json.load(file)
        else:
            with open(self.filename, 'w') as file:
                json.dump({}, file)
            self.database = {}
        print(f'[{datetime.now()}]: База данных успешно загружена!')

    def add_record(self, record_id=None, data=None):
        for existing_record_id, existing_data in self.database.items():
            if existing_data == data:
                return

        if record_id is None:
            record_id = max(int(key) for key in self.database.keys()) + 1 if self.database.keys() else 0

        self.database[str(record_id)] = data
        self.save_database()

        print(f'[{datetime.now()}]: В базу данных добавлена запись: {self.get_record(str(record_id))}')

    def get_record(self, record_id=None):
        if record_id is not None:
            return self.database.get(str(record_id))
        else:
            return self.database

    def get_all_records(self):
        return list(self.database.values())

    def save_database(self):
        with open(self.filename, 'w') as file:
            json.dump(self.database, file)
