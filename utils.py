import asyncio
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

async def get_movie_id(id:str = "666") -> Tuple[Dict[str, Any], int]:
    """
    Асинхронный запрос.
    Получить информацию о фильмы по kp id
    :return: Информация о фильме
    """
    # param_request = {"id": id}
    url = f"{BASEURL}/v1.3/movie/{str(id)}"
    # response = requests.get(url, headers=headers, params=param_request)
    response = requests.get(url, headers=headers)
    date = json.loads(response.text)
    return date, response.status_code

if __name__ == "__main__":
    adata, code = asyncio.run(get_movie_id(id=str(4647040)))
    # data_film = adata["docs"]


    with open('json_data.json', 'w', encoding='UTF-8') as file:
        json.dump(adata, file, indent=4)

    # with open('json_data.json', 'r') as file:
    #     data = json.load(file)
    #
    # name_film = data['name']
    # names_film = data['names']
    # rating_kp_film = data['rating']['kp']
    # rating_imdb_film = data['rating']['imdb']
    # age_rating_film = data['ageRating']
    # poster_film = data['poster']['url']
    # description_film = data['description']
    # type_film = data['type']
    # slogan_film = data['slogan']
    # year_film = data['year']
    # print('Название:', name_film)
    # # print(*names_film)
    # print("Рейтинг КП:", rating_kp_film, "Рейтинг IMDB:", rating_imdb_film)
    # print("Год производства:", year_film)
    # print("Возрастное ограничение:", age_rating_film)
    # print("Жанр:", type_film)
    # print("Постер:", poster_film)
    # print("Краткое содержание:", description_film)
    # print("Слоган:", slogan_film)
