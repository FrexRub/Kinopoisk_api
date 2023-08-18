import asyncio
import json

from kinopoisk_dev import KinopoiskDev
from kinopoisk_dev.model import Movie

from settings import SiteSettings

site = SiteSettings()

TOKEN = site.api_key.get_secret_value()


async def get_movie_async() -> Movie:
    """
    Асинхронный запрос.
    Получить информацию о фильмы по kp id
    :return: Информация о фильме
    """
    kp = KinopoiskDev(token=TOKEN)
    return await kp.afind_one_movie(666)


def get_movie() -> Movie:
    """
    Синхронный запрос.
    Получить информацию о фильмы по kp id
    :return: Информация о фильме
    """
    kp = KinopoiskDev(token=TOKEN)
    return kp.find_one_movie(666)


if __name__ == "__main__":
    adata = asyncio.run(get_movie_async())
    # data = get_movie()

    print(adata.json().encode('utf8'))
    with open('json_data.json', 'w') as file:
        # json.dump(adata, file)
        file.write(adata.json(indent=4))