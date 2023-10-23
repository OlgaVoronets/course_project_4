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

    def delete_file(self, filename):
        pass

    def clear_file(self, filename):
        pass


class JSONSaver(Saver):
    """Класс для операций с файлом в формате json"""

    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        """открывает файл json, возвращает содержимое"""
        with open(self.filename, encoding='utf8') as f:
            return json.load(f)

    def save_to_file(self, collection):
        """Принимает список объектов класса и записывает в файл их str"""
        list_to_save = []
        with open(self.filename, 'a', encoding='utf8') as file:
            for el in collection:
                list_to_save.append(json.dumps(str(el), ensure_ascii=False))
            file.write(json.dumps(list_to_save, indent=4, ensure_ascii=False))


    def delete_file(self, filename):
        os.remove(filename)

    def clear_file(self, filename):
        with open(filename, 'w', encoding='utf8') as file:
            json.dump({}, file)
