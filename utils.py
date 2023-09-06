import asyncio
import json
import requests

from settings import SiteSettings

site = SiteSettings()
BASEURL = "https://api.kinopoisk.dev"
headers = {
    "accept": "application/json",
    "X-API-KEY": site.api_key.get_secret_value()
}



async def get_movie_async():
    """
    Асинхронный запрос.
    Получить информацию о фильмы по kp id
    :return: Информация о фильме
    """
    id = 666
    url = f"{BASEURL}/v1.3/movie/{id}"
    print(url, headers)
    # text_querystring = {"languagecode": "ru"}
    # text_querystring["text"] = name_city
    response = requests.get(url, headers=headers)
    # response = requests.get(url, headers=headers, params=text_querystring)
    date = json.loads(response.text)
    return date

if __name__ == "__main__":
    adata = asyncio.run(get_movie_async())
    # data = get_movie()
    print(adata)

    # print(adata.json().encode('utf8'))
    # with open('json_data.json', 'w', encoding='UTF-8') as file:
    #     file.write(adata.json(indent=4))

    with open('json_data.json', 'r') as file:
        data = json.load(file)

    name_film = data['name']
    names_film = data['names']
    print(name_film)
    print(*names_film)