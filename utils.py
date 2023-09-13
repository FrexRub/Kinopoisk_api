import json
import requests
from typing import Dict, Any, Tuple

from settings import SiteSettings

site = SiteSettings()
BASEURL = "https://api.kinopoisk.dev"
headers = {
    "accept": "application/json",
    "X-API-KEY": site.api_key.get_secret_value()
}


def get_movie_id(id: str = "666") -> Tuple[Dict[str, Any], int]:
    """Получить информацию о фильмы по kp id
    :param id: номер фильма
    :type id: str

    :return: Информация о фильме и коде состояния
    :type: Tuple[Dict[str, Any], int]
    """
    url = f"{BASEURL}/v1.3/movie/{str(id)}"
    response = requests.get(url, headers=headers)
    date = json.loads(response.text)
    return date, response.status_code


def get_movie_random() -> Tuple[Dict[str, Any], int]:
    """Получить информацию о случайном фильме
    :return: Информация о фильме и коде состояния
    :type: Tuple[Dict[str, Any], int]
    """
    url = f"{BASEURL}/v1.3/movie/random"
    response = requests.get(url, headers=headers)
    date = json.loads(response.text)
    return date, response.status_code


def get_rating_film(rating: str = '7-9') -> Tuple[Dict[str, Any], int]:
    """Возврат списка фильмов по заданному рейтингу
    :param rating: диапазон рейтингов
    :type rating: str

    :return: сведения о фильмах, код выполнения запроса
    :type: Tuple[Dict[str, Any], int]
    """
    param_request = {
        "page": "1",
        "limit": "10",
        "rating.kp": rating
    }
    url = f"{BASEURL}/v1.3/movie"
    response = requests.get(url, headers=headers, params=param_request)
    date = json.loads(response.text)

    return date, response.status_code


def get_moive_name(name_film: str = "Тор") -> Tuple[Dict[str, Any], int]:
    """Возврат списка фильмов, содержащих в названии запрошенный текст
   :param name_film: название фильма
   :type name_film: str

   :return: сведения о фильмах, код выполнения запроса
   :type: Tuple[Dict[str, Any], int]
   """
    param_request = {
        "page": "1",
        "limit": "10",
        "query": name_film
    }
    url = f"{BASEURL}/v1.2/movie/search"
    response = requests.get(url, headers=headers, params=param_request)
    date = json.loads(response.text)

    return date, response.status_code


if __name__ == "__main__":
    get_moive_name()
