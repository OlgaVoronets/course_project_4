from api_clients import HeadHunterApi, SuperJobApi
from saver_to_file import JSONSaver
from vacancy import Vacancy
import utils

"""Функция для взаимодействия с пользователем"""


def create_user_request(answer, keyword):
    """Отправляем запрос и сохраняем полученные данные в файлы"""
    if answer == '1':
        utils.get_hh_vacancies(keyword)
    elif answer == '2':
        utils.get_sj_vacancies(keyword)
    elif answer == '3':
        utils.get_hh_vacancies(keyword)
        utils.get_sj_vacancies(keyword)


print('Выберите платформу, с которой необходимо получить данные о вакансиях:\n'
      '1 - Head Hunter\n'
      '2 - Super Job\n'
      '3 - Обе платформы\n')
answer = input()
keyword = input('Введите поисковый запрос: \n')

"""Создаем поисковый запрос"""
create_user_request(answer, keyword)

data = Vacancy.all.copy()
print('Введите город для отбора вакансий, либо нажмите Enter, чтобы пропустить')
area = input()
if area != '':
    for dict_ in data:
        if dict_.area == area:
            print(dict_)
print()

print('Сортировать вакансии по зарплате? да / нет')

answer = input()
if answer == 'да':
    for dict_ in sorted(data):
        print(dict_)

print('Вывести ТОП по зарплате? да / нет')
answer = input()
if answer == 'да':
    print('Укажите количество вакансий для вывода')
    answer = int(input())
    if answer > len(data):
        answer = len(data)
    data = sorted(data)
    for dict_ in data[-answer:]:
        print(dict_)

saver = JSONSaver()
saver.save_to_file(data, Vacancy.collection_filename)

print(f'Выборка вакансий сохранена в файл {Vacancy.collection_filename}')

saver.delete_file(HeadHunterApi.file_to_save)
saver.clear_file(SuperJobApi.file_to_save)
