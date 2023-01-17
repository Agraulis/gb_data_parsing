from pymongo import MongoClient
import json
import pprint

DESIRED_SALARY = 40000


def get_vacancy_list():
    with open("../lesson_3/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def add_new_vacancy(vacancy_collection):
    for offer in get_vacancy_list():
        duplicates = vacancy_collection.find({"link": offer["link"]})
        # если такой ссылки нет в БД, то добавим вакансию в БД
        if not len(list(duplicates)):
            vacancy_collection.insert_one(offer)


def print_vacancy_with_desired_salary(vacancy_collection, salary):
    """
    Выведем на экран те вакансии, где начало диапазона зарплат ("от...")
    больше, чем аргумент salary
    :param vacancy_collection: коллекция, в которой выполняем поиск
    :param salary: минимальная желаемая зарплата
    :return: None
    """
    for vacancy in vacancy_collection.find():
        if "от" in vacancy["salary"] and int(vacancy["salary"].split()[1]) >= salary:
            pprint.pprint(vacancy)


client = MongoClient()
db = client.hh
add_new_vacancy(db.vacancy)
print_vacancy_with_desired_salary(db.vacancy, DESIRED_SALARY)
