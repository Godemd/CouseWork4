import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vac1():
    vac_data = {
        "id": "98707107",
        "premium": False,
        "name": "Разработчик С++",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {"id": "99", "name": "Уфа", "url": "https://api.hh.ru/areas/99"},
        "salary": {"from": 300000, "to": None, "currency": "RUR", "gross": True},
        "type": {"id": "open", "name": "Открытая"},
        "address": {"raw": "Уфа, улица Джалиля Киекбаева, 2"},
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2024-05-11T17:53:15+0300",
        "created_at": "2024-05-11T17:53:15+0300",
        "archived": True,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=98707107",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/98707107?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/98707107",
        "relations": [],
        "employer": {
            "id": "10384591",
            "name": "Лаборатория Современных Цифровых Технологий",
            "url": "https://api.hh.ru/employers/10384591",
            "alternate_url": "https://hh.ru/employer/10384591",
            "logo_urls": {
                "240": "https://img.hhcdn.ru/employer-logo/6601822.jpeg",
                "90": "https://img.hhcdn.ru/employer-logo/6601821.jpeg",
                "original": "https://img.hhcdn.ru/employer-logo-original/1245348.jpg",
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10384591",
            "accredited_it_employer": True,
            "trusted": True,
        },
        "snippet": {"requirement": None, "responsibility": None},
        "contacts": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "accept_incomplete_resumes": False,
        "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
        "employment": {"id": "full", "name": "Полная занятость"},
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None,
    }
    return Vacancy(vacancy_data=vac_data)


@pytest.fixture
def vac1_2():
    vac_data = {
        "id": "104434417",
        "premium": False,
        "name": "Golang Developer (Уфа)",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {"id": "99", "name": "Уфа", "url": "https://api.hh.ru/areas/99"},
        "salary": {"from": 300000, "to": None, "currency": "RUR", "gross": False},
        "type": {"id": "open", "name": "Открытая"},
        "address": {
            "city": "Уфа",
            "street": "улица 50-летия Октября",
            "building": "13/2",
            "lat": 54.73789042963892,
            "lng": 55.96776333862268,
            "description": None,
            "raw": "Уфа, улица 50-летия Октября, 13/2",
            "metro": None,
            "metro_stations": [],
            "id": "3436804",
        },
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2024-07-23T11:56:16+0300",
        "created_at": "2024-07-23T11:56:16+0300",
        "archived": False,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=104434417",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/104434417?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/104434417",
        "relations": [],
        "employer": {
            "id": "1480667",
            "name": "Тагес Джамп",
            "url": "https://api.hh.ru/employers/1480667",
            "alternate_url": "https://hh.ru/employer/1480667",
            "logo_urls": {
                "90": "https://img.hhcdn.ru/employer-logo/3915579.png",
                "240": "https://img.hhcdn.ru/employer-logo/3915580.png",
                "original": "https://img.hhcdn.ru/employer-logo-original/868676.png",
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1480667",
            "accredited_it_employer": True,
            "trusted": True,
        },
        "snippet": {
            "requirement": (
                "Уверенно знаете Go. Понимаете, что такое ООП, шаблоны проектирования. "
                "Знакомы с основными алгоритмами, структурами данных. Понимаете необходимости и умение покрывать..."
            ),
            "responsibility": (
                "TAGES работает на рынке IT с 2012 года. Компания занимается проектированием, разработкой и "
                "поддержкой digital-решений для автоматизации бизнеса. "
            ),
        },
        "contacts": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "accept_incomplete_resumes": False,
        "experience": {"id": "between3And6", "name": "От 3 до 6 лет"},
        "employment": {"id": "full", "name": "Полная занятость"},
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None,
    }
    return Vacancy(vacancy_data=vac_data)


@pytest.fixture
def vac2():
    vac_data = {
        "id": "98707107",
        "premium": False,
        "name": "Разработчик С++",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {"id": "99", "name": "Уфа", "url": "https://api.hh.ru/areas/99"},
        "salary": {"from": 1300000, "to": None, "currency": "RUR", "gross": True},
        "type": {"id": "open", "name": "Открытая"},
        "address": {"raw": "Уфа, улица Джалиля Киекбаева, 2"},
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2024-05-11T17:53:15+0300",
        "created_at": "2024-05-11T17:53:15+0300",
        "archived": True,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=98707107",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/98707107?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/98707107",
        "relations": [],
        "employer": {
            "id": "10384591",
            "name": "Лаборатория Современных Цифровых Технологий",
            "url": "https://api.hh.ru/employers/10384591",
            "alternate_url": "https://hh.ru/employer/10384591",
            "logo_urls": {
                "240": "https://img.hhcdn.ru/employer-logo/6601822.jpeg",
                "90": "https://img.hhcdn.ru/employer-logo/6601821.jpeg",
                "original": "https://img.hhcdn.ru/employer-logo-original/1245348.jpg",
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10384591",
            "accredited_it_employer": True,
            "trusted": True,
        },
        "snippet": {"requirement": None, "responsibility": None},
        "contacts": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "accept_incomplete_resumes": False,
        "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
        "employment": {"id": "full", "name": "Полная занятость"},
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None,
    }
    return Vacancy(vacancy_data=vac_data)
