from datetime import date
from collections import defaultdict
import pandas


def count_winery_age(YEAR_OF_FOUNDATION) -> str:
    """
    calculates the lifetime of the winery

    :return f"{time} лет"

    """
    winery_age = date.today().year - YEAR_OF_FOUNDATION
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
    wines = wine_descriptions.to_dict("records")
    for wine in wines:
        wine_database[wines[wine]["Категория"]].append(wines[wine])
    return dict(wine_database)


def find_min_price() -> int:
    """
    returns minimal price of vine
    """
    wine_descriptions = pandas.read_excel('wine3.xlsx', sheet_name="Лист1", keep_default_na=False)
    min_price = min(wine_descriptions["Цена"].to_list())
    return min_price

