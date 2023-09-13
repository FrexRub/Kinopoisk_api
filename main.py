import asyncio

from utils import get_movie_id, get_movie_random, get_rating_film, get_moive_name, message_short_info_film
from messages import message_err, message_no_id, message_info_film


async def movie_id() -> None:
    print("Информация  о фильме по его номеру (id)\n")
    input_text: str = input("Введите номер (id) фильма: ")
    if input_text.isdigit():
        adata, code = get_movie_id(id=input_text)

        if code != 200:
            message_err(code)
        elif adata.get("id") is None:
            message_no_id()
        else:
            message_info_film(adata)
    else:
        print("Необходимо ввести положительное целое число")


async def movie_rating() -> None:
    print("Информация  о фильмах с рейтингами в запрошенном диапазоне\n")
    input_text: str = input("Введите интересуемый диапазон рейтинга (7-9): ")
    adata, code = get_rating_film(rating=input_text)

    if code != 200:
        message_err(code)
    # elif adata.get("id") is None:
    #     message_no_id()
    else:
        count = 0
        for i_date in adata["docs"]:
            count += 1
            print(count, end='. ')
            message_info_film(i_date)
            print('=' * 15)


async def movie_random() -> None:
    adata, code = get_movie_random()

    if code != 200:
        message_err(code)
    elif adata.get("id") is None:
        message_no_id()
    else:
        print(f"Информация  о фильме c номером {adata.get('id')}\n")
        message_info_film(adata)


async def movie_name_film() -> None:
    """Информация о фильмах, содержащих в названии запрошенный текст"""
    print("Информация  о фильмах по названию\n")
    input_text: str = input("Введите название фильма: ")
    adata, code = get_moive_name(name_film=input_text)

    if code != 200:
        message_err(code)
    # elif adata.get("id") is None:
    #     message_no_id()
    else:
        print(f"Информация  о найденных фильмах c названием {input_text}\n")
        for i_date in adata["docs"]:
            message_short_info_film(i_date)
            print('\n')
            print('=' * 15)


# Press the green button in the gutter to run the script.
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
