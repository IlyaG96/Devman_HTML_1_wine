import pandas
from datetime import date
from collections import defaultdict


def count_winery_age(YEAR_OF_FOUNDATION: int) -> str:
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


def make_wine_database(PATH_TO_DATABASE: str) -> dict:
    """
    returns a dictionary containing information about wines and drinks from wine.xslx using pandas

    :return dict
    """
    wine_database = defaultdict(list)
    wine_descriptions = pandas.read_excel(PATH_TO_DATABASE, sheet_name="Лист1", keep_default_na=False)
    wine_descriptions = wine_descriptions.sort_index()
    wines = wine_descriptions.to_dict("records")
    for wine_num, wine in enumerate(wines):
        wine_database[wines[wine_num]["Категория"]].append(wines[wine_num])
    return wine_database


