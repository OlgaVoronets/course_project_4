class Vacancy:
    all = []
    collection_filename = 'received_vacancies.json'

    def __init__(self, name, url, area, salary, requirement):
        self.name = name
        self.url = url
        self.area = area
        self.salary = salary
        if salary:
            if salary['from']:
                self.salary_from = self.salary['from']
            else:
                if salary['to']:
                    self.salary_from = self.salary['to']
            self.salary_currency = self.salary['currency']

        self.salary_from = 0
        self.salary_to = 0
        self.salary_currency = None
        self.requirement = requirement
        self.all.append(self)

    def __str__(self):
        result = f'{self.name}, {self.area}\nЗарплата '
        if self.salary:
            if self.salary_from > 0:
                result += f'от {self.salary_from} '
            result += f'{self.salary_currency}'
        else:
            result += 'не указана'
        result += f'\nСсылка на вакансию: {self.url}\n{self.requirement}'
        return result

    def __gt__(self, other):
        """Сравнение по минимальной зарплате"""
        return self.salary_from > other.salary_from

    def __lt__(self, other):
        """Сравнение по минимальной зарплате"""
        return self.salary_from < other.salary_from


