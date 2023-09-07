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
    param_request = {"id": id}
    url = f"{BASEURL}/v1.3/movie"
    response = requests.get(url, headers=headers, params=param_request)
    date = json.loads(response.text)
    return date, response.status_code

if __name__ == "__main__":
    adata, code = asyncio.run(get_movie_id(id=str(666)))
    data_film = adata["docs"]
    for i_key, i_val in adata.items():
        print(i_key, i_val)
    for i_list in data_film:
        print(i_list)

    # with open('json_data.json', 'w', encoding='UTF-8') as file:
    #     json.dump(adata, file, indent=4)

    with open('json_data.json', 'r') as file:
        data = json.load(file)

    name_film = data['name']
    names_film = data['names']
    print(name_film)
    print(*names_film)