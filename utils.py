from api_clients import HeadHunterApi, SuperJobApi
from vacancy import Vacancy
from saver_to_file import JSONSaver

def get_HH_vacancies(keyword):
    """Создает экземпляры класса Вакансий из файла HH и добавляет их в общий список класса"""
    hh = HeadHunterApi(keyword)
    data = hh.get_response()
    hh.add_to_json(data)
    data = JSONSaver().open_file(hh.file_to_save)
    for dict_ in data:
        Vacancy(dict_['name'], dict_['url'], dict_['area'], dict_.get('salary'), dict_['requirement'])


def get_SJ_vacancies(keyword):
    """Создает экземпляры класса Вакансий из файла SJ и добавляет их в общий список класса"""
    sj = SuperJobApi(keyword)
    data = sj.get_response()
    sj.add_to_json(data)
    data = JSONSaver().open_file(sj.file_to_save)
    for dict_ in data:
        Vacancy(dict_['name'], dict_['url'], dict_['area'], dict_.get('salary'), dict_['requirement'])
