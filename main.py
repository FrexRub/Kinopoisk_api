import asyncio
import json

from utils import get_movie_id, get_movie_random
from messages import message_err, message_no_id, message_info_film


async def movie_id() -> None:
    print("Информация  о фильме по его номеру (id)\n")
    input_text: str = input("Введите номер (id) фильма: ")
    if input_text.isdigit():
        adata, code = get_movie_id(id=input_text)
        # adata, code = asyncio.run(get_movie_id(id=str(4647040)))

        # with open('json_data.json', 'r') as file:
        #     adata = json.load(file)
        # code = 200

        if code != 200:
            message_err(code)
        elif adata.get("id") is None:
            message_no_id()
        else:
            message_info_film(adata)
    else:
        print("Необходимо ввести положительное целое число")


async def movie_random() -> None:
    adata, code = get_movie_random()

    if code != 200:
        message_err(code)
    elif adata.get("id") is None:
        message_no_id()
    else:
        print(f"Информация  о фильме c номером {adata.get('id')}\n")
        message_info_film(adata)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        print('Кинопоиск. Получение информации о фильмах с сайта "Кинопоиск"\n')
        print("1. Информация  о фильме по его номеру (id)")
        print("2. Информации о фильме, выбранном случайным образом.")
        print("3. Выйти из программы\n")
        num_item: str = input("Укажите номе пункта: ")
        if num_item == '1':
            asyncio.run(movie_id())
        elif num_item == '2':
            asyncio.run(movie_random())
        elif num_item == '3':
            break
