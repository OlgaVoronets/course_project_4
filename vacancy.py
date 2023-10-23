class Vacancy:
    all = []
    collection_filename = 'received_vacancies.json'

    def __init__(self, name, url, area, salary, requirement):
        self.name = name
        self.url = url
        self.area = area

        if not salary:
            self.salary_from = 0
            self.salary_to = 0
            self.salary_currency = None
        else:
            self.salary_from = salary.get('from')
            self.salary_to = salary.get('to')
            self.salary_currency = salary.get('currency')

        self.requirement = requirement
        self.all.append(self)

    def __str__(self):
        result = f'{self.name}, {self.area}\nЗарплата '
        # if self.salary:
        if self.salary_from != None and self.salary_from > 0:
            result += f'от {self.salary_from} '
        if self.salary_to != None and self.salary_to > 0:
            result += f'до {self.salary_to} '
        if self.salary_currency:
            result += f'{self.salary_currency}'
        else:
            result += 'не указана'
        result += f'\nСсылка на вакансию: {self.url}\n'
        return result

    def __gt__(self, other):
        """Сравнение по минимальной зарплате"""
        if self.salary_from is None:
            self.salary_from = 0
        elif other.salary_from is None:
            other.salary_from = 0
        return self.salary_from > other.salary_from

    def __lt__(self, other):
        """Сравнение по минимальной зарплате"""
        if self.salary_from is None:
            self.salary_from = 0
        elif other.salary_from is None:
            other.salary_from = 0
        return self.salary_from < other.salary_from


