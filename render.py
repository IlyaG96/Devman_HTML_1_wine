from datetime import date
from collections import defaultdict
import pandas


def time_of_life() -> str:
    """returns the age of the winery"""
    year_of_foundation = 1920
    time = date.today().year - year_of_foundation
    if str(time).endswith("2" or "3"):
        return f"{time} года"
    elif str(time).endswith("1"):
        return f"{time} год"
    else:
        return f"{time} лет"


def make_wine_database() -> dict:
    """returns a dictionary containing information about wines and drinks"""
    wine_database = defaultdict(list)
    wine_descriptions = pandas.read_excel('wine3.xlsx', sheet_name="Лист1", keep_default_na=False)
    wine_descriptions = wine_descriptions.sort_index()
    wine_list = wine_descriptions.to_dict("records")
    for i in range(len(wine_list)):
        wine_database[wine_list[i]["Категория"]].append(wine_list[i])
    return dict(wine_database)


def find_min_price() -> int:
    """returns minimal price of vine"""
    wine_descriptions = pandas.read_excel('wine3.xlsx', sheet_name="Лист1", keep_default_na=False)
    min_price = min(wine_descriptions["Цена"].to_list())
    return min_price

