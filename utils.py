import asyncio
import json
import requests
from typing import Dict, Any, Tuple

from messages import message_info_film
from settings import SiteSettings

site = SiteSettings()
BASEURL = "https://api.kinopoisk.dev"
headers = {
    "accept": "application/json",
    "X-API-KEY": site.api_key.get_secret_value()
}

def get_movie_id(id:str = "666") -> Tuple[Dict[str, Any], int]:
    """
    Получить информацию о фильмы по kp id
    :return: Информация о фильме и коде состояния
    """
    # param_request = {"id": id}
    url = f"{BASEURL}/v1.3/movie/{str(id)}"
    # response = requests.get(url, headers=headers, params=param_request)
    response = requests.get(url, headers=headers)
    date = json.loads(response.text)
    return date, response.status_code


def get_movie_random() -> Tuple[Dict[str, Any], int]:
    """
    Получить информацию о случайном фильме
    :return: Информация о фильме и код состояния
    """
    url = f"{BASEURL}/v1.3/movie/random"
    response = requests.get(url, headers=headers)
    date = json.loads(response.text)
    return date, response.status_code

def any_quest() -> None:
    param_request = {
        "page": "1",
        "limit": "10",
        "rating.kp": "7-9"
    }
    url = f"{BASEURL}/v1.3/movie"
    response = requests.get(url, headers=headers, params=param_request)
    date = json.loads(response.text)
    print(response.url)
    for i_date in date["docs"]:
        message_info_film(i_date)
        print('\n', '=' * 15)



if __name__ == "__main__":
    any_quest()
    # adata, code = asyncio.run(get_movie_id(id=str(4647040)))
    # # data_film = adata["docs"]
    #
    #
    # with open('json_data.json', 'w', encoding='UTF-8') as file:
    #     json.dump(adata, file, indent=4)

    # with open('json_data.json', 'r') as file:
    #     data = json.load(file)
    #

