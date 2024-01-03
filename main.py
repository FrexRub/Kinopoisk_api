import asyncio
from typing import List

import sentry_sdk

from utils import get_movie_id, get_movie_random, get_rating_film, get_moive_name
from messages import message_err, message_no_id, message_info_film, message_short_info_film

sentry_sdk.init(
    dsn="https://4bdeac5ba1bc8b6637c3a99d14591aa1@o4506468033495040.ingest.sentry.io/4506508206997504",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


async def movie_id() -> None:
    """Пункт меню: Информация  о фильме по его номеру"""
    print("Информация  о фильме по его номеру (id)\n")
    input_text: str = input("Введите номер (id) фильма: ")
    if input_text.isdigit():
        adata, code = get_movie_id(id=input_text)

        if code != 200:
            message_err(code, adata)
        elif adata.get("id") is None:
            message_no_id()
        else:
            message_info_film(adata)
    else:
        print("\n!!!Необходимо ввести положительное целое число\n")


def valid_input_rating(rating: str) -> bool:
    """Проверяет валидность введенного диапазона рейтингов"""
    result: bool = True
    list_rating: List[str] = rating.split('-')
    if len(list_rating) != 2:
        result = False
    else:
        result = list_rating[0].isdigit() and list_rating[1].isdigit()
        if result:
            result = int(list_rating[1]) > int(list_rating[0])
    return result


async def movie_rating() -> None:
    """Пункт меню: Список фильмов по заданному диапазону рейтинга"""
    print("Информация  о фильмах с рейтингами в запрошенном диапазоне\n")
    input_text: str = input("Введите интересуемый диапазон рейтинга (например 7-9): ")
    if valid_input_rating(input_text):
        adata, code = get_rating_film(rating=input_text)

        if code != 200:
            message_err(code, adata)
        # elif adata.get("id") is None:
        #     message_no_id()
        else:
            count = 0
            for i_date in adata["docs"]:
                count += 1
                print(count, end='. ')
                message_info_film(i_date)
                print('=' * 15)
    else:
        print("\n!!!Рейтинг должен задаваться диапазоном цифр (например: 7-9)\n")


async def movie_random() -> None:
    """Пункт меню: Информации о фильме, выбранном случайным образом"""
    adata, code = get_movie_random()

    if code != 200:
        message_err(code, adata)
    elif adata.get("id") is None:
        message_no_id()
    else:
        print(f"Информация  о фильме c номером {adata.get('id')}\n")
        message_info_film(adata)


async def movie_name_film() -> None:
    """Пункт меню: Поиск информации о фильме по наименованию"""
    print("Информация  о фильмах по названию\n")
    input_text: str = input("Введите название фильма: ")
    adata, code = get_moive_name(name_film=input_text)

    if code != 200:
        message_err(code, adata)
    else:
        print(f"Информация  о найденных фильмах c названием {input_text}\n")
        for i_date in adata["docs"]:
            if input_text in i_date["name"]:
                message_short_info_film(i_date)
                print('\n')
                print('=' * 15)


if __name__ == '__main__':
    while True:
        print('Кинопоиск. Получение информации о фильмах с сайта "Кинопоиск"\n')
        print("1. Информация  о фильме по его номеру (id)")
        print("2. Информации о фильме, выбранном случайным образом.")
        print("3. Список фильмов по заданному диапазону рейтинга (7-9).")
        print("4. Поиск информации о фильме по наименованию.")
        print("0. Выйти из программы\n")
        num_item: str = input("Укажите номе пункта: ")
        if num_item == '1':
            asyncio.run(movie_id())
        elif num_item == '2':
            asyncio.run(movie_random())
        elif num_item == '3':
            asyncio.run(movie_rating())
        elif num_item == '4':
            asyncio.run(movie_name_film())
        elif num_item == '0':
            break
