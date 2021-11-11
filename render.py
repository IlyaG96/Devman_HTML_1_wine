from datetime import date
from collections import defaultdict
import pandas


def count_winery_age() -> str:
    """
    calculates the lifetime of the winery

    :return f"{time} лет"

    """
    year_of_foundation = 1920
    winery_age = date.today().year - year_of_foundation
    if str(winery_age).endswith("2" or "3"):
        return f"{winery_age} года"
    elif str(winery_age).endswith("1"):
        return f"{winery_age} год"
    else:
        return f"{winery_age} лет"


def make_wine_database() -> dict:
    """
    returns a dictionary containing information about wines and drinks from wine.xslx using pandas

    :return dict
    """
    wine_database = defaultdict(list)
    wine_descriptions = pandas.read_excel('wine3.xlsx', sheet_name="Лист1", keep_default_na=False)
    wine_descriptions = wine_descriptions.sort_index()
    wine_list = wine_descriptions.to_dict("records")
    for i in range(len(wine_list)):
        wine_database[wine_list[i]["Категория"]].append(wine_list[i])
    return dict(wine_database)


def find_min_price() -> int:
    """
    returns minimal price of vine
    """
    wine_descriptions = pandas.read_excel('wine3.xlsx', sheet_name="Лист1", keep_default_na=False)
    min_price = min(wine_descriptions["Цена"].to_list())
    return min_price

