import json
import logging.config
import requests
from typing import Dict, Any, Tuple

from settings import SiteSettings, dict_config

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
    logger.info(f'Начло поиска фильма по id: {id}')
    url = f"{BASEURL}/v1.3/movie/{id}"
    try:
        response: requests.Response = requests.get(url, headers=headers)
    except Exception as exp:
        logger.exception(exp)
    else:
        date = json.loads(response.text)
        if response.status_code == 200:
            logger.info(f'Код выполнения поиска {response.status_code}')
        else:
            logger.warning(f'Код выполнения поиска {response.status_code}')
        return date, response.status_code


def get_movie_random() -> Tuple[Dict[str, Any], int]:
    """Получить информацию о случайном фильме
    :return: Информация о фильме и коде состояния
    :type: Tuple[Dict[str, Any], int]
    """
    logger.info("Запуск поиска случайного фильма")
    url = f"{BASEURL}/v1.3/movie/random"
    try:
        response: requests.Response = requests.get(url, headers=headers)
    except Exception as exp:
        logger.exception(exp)
    else:
        if response.status_code == 200:
            logger.info(f'Код выполнения поиска {response.status_code}')
        else:
            logger.warning(f'Код выполнения поиска {response.status_code}')
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
    logger.info(f'Начало поиска фильма по рейтингу: {rating}')
    url = f"{BASEURL}/v1.3/movie"
    try:
        response: requests.Response = requests.get(url, headers=headers, params=param_request)
    except Exception as exp:
        logger.exception(exp)
    else:
        if response.status_code == 200:
            logger.info(f'Код выполнения поиска {response.status_code}')
        else:
            logger.warning(f'Код выполнения поиска {response.status_code}')
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
    logger.info(f'Начало поиска фильма по имени: {name_film}')
    url = f"{BASEURL}/v1.2/movie/search"
    try:
        response: requests.Response = requests.get(url, headers=headers, params=param_request)
    except Exception as exp:
        logger.exception(exp)
    else:
        if response.status_code == 200:
            logger.info(f'Код выполнения поиска {response.status_code}')
        else:
            logger.warning(f'Код выполнения поиска {response.status_code}')
        date = json.loads(response.text)
        return date, response.status_code


logging.config.dictConfig(dict_config)
logger = logging.getLogger('utils')

if __name__ == "__main__":
    get_moive_name()
