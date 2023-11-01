import json
from abc import ABC, abstractmethod
import requests
import os


class APIClient(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_response(self, *args, **kwargs):
        """Создать запрос, вернуть json со списком словарей"""
        pass

    @abstractmethod
    def add_to_json(self, *args, **kwargs):
        """Сохранить данные в файл"""
        pass


class HeadHunterApi(APIClient):
    """Класс для получения вакансий с платформы HeadHunter"""
    file_to_save = 'HH_vacancies.json'
    url = "https://api.hh.ru/vacancies"
    headers = {"User-Agent": "AnyApp/1.0"}

    def __init__(self, keyword=None):
        self.params = {"text": keyword}

    def get_response(self):
        """создает запрос на платформу и получает список словарей с вакансиями в json-формате"""
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.json()['items']

    def add_to_json(self, data, filename=file_to_save):
        """Сохраняет данные из списка словарей в заданном формате """
        with open(filename, 'w', encoding='utf8') as file:
            data_list = []
            for dict_ in data:
                temp_dict = {'name': dict_['name'], 'area': dict_['area']['name'],
                             'salary': dict_.get('salary'), 'url': dict_['alternate_url'],
                             'requirement': dict_['snippet']['requirement']}
                data_list.append(temp_dict)
            json.dump(data_list, file, indent=2, ensure_ascii=False)



class SuperJobApi(APIClient):
    """Класс для получения вакансий с платформы SuperJob"""
    API_KEY = os.getenv('SuperJobAppSecretKey')
    HEADERS = {'X-Api-App-Id': API_KEY}
    file_to_save = 'SJ_vacancies.json'
    url = "https://api.superjob.ru/2.0/vacancies/"

    def __init__(self, keyword=None):
        self.params = {'keyword': keyword}

    def get_response(self, area=None, keyword=None, quantity=1):
        """создает запрос на платформу и получает список словарей с вакансиями в json-формате"""
        response = requests.get(self.url, params=self.params, headers=self.HEADERS)
        return response.json()['objects']

    def add_to_json(self, data, filename=file_to_save):
        """Сохраняет данные из списка словарей в заданном формате"""
        with open(filename, 'w', encoding='utf8') as file:
            data_list = []
            for dict_ in data:
                temp_dict = {"name": dict_["profession"], 'area': dict_["town"]["title"],
                             "salary": {'from': dict_["payment_from"], 'to': dict_["payment_to"],
                                        "currency": dict_["currency"]}, 'url': dict_['link'],
                             'requirement': dict_["candidat"]}
                data_list.append(temp_dict)
            json.dump(data_list, file, indent=2, ensure_ascii=False)

