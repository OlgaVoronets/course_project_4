import json
import os
from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс для операций с файлами"""
    @abstractmethod
    def open_file(self):
        pass

    def save_to_file(self, collection):
        pass

    def delete_file(self):
        pass

    def clear_file(self):
        pass


class JSONSaver(Saver):
    """Класс для операций с файлом в формате json"""

    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        with open(self.filename, encoding='utf8') as f:
            return json.load(f)

    def save_to_file(self, collection):
        with open(self.filename, 'w', encoding='utf8') as file:
            json.dump(collection, file, indent=2, ensure_ascii=False)

    def delete_file(self):
        os.remove(self.filename)

    def clear_file(self):
        with open(self.filename, 'w', encoding='utf8') as file:
            json.dump({}, file)
