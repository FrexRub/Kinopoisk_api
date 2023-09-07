from pprint import pprint
from typing import Dict, Any, List, NamedTuple

class Person(NamedTuple):
    id: int
    photo: str
    name: str
    profession: str

def get_info_person(data: Dict[str, Any]) -> Dict[str, List[Person]]:
    """Выборка информации по актерам, режисерам"""
    persons_film: List[Dict[str, str|int]] = data["docs"][0]["persons"]
    dict_persons: Dict[str, List[Person]] = {"actor": [], "director": []}
    for i_dic in persons_film:
        i_person = Person(id=i_dic["id"], photo=i_dic["photo"],
                          name=i_dic["name"], profession=i_dic["profession"])
        dict_persons[i_dic["profession"]].append(i_person)
    return dict_persons


def get_info_genres(data: Dict[str, Any]) -> str:
    """Выборка информации по актерам, режисерам"""
    genres_film: List[Dict[str, str]] = data["docs"][0]["genres"]
    result_list: List[str] = list()
    for i_data in genres_film:
        result_list.append(i_data["name"])
    return ','.join(result_list)


async def message_err(cod_err: int) -> None:
    """Вывод сообщения об ошибке"""
    print(f"Что-то пошло не так: {cod_err}")


async def message_no_id() -> None:
    """Вывод сообщения об отсутствие id"""
    print(f"По этому id ничего не найдено!")


async def message_info_film(data: Dict[str, Any]) -> None:
    """Вывод сообщения об отсутствие id"""
    data_film: Dict[str, Any] = data["docs"][0]

    for i_key in data_film.keys():
        print(i_key)

    print(data["docs"])
    print("-"*20)
    print(data["docs"][0])
    print("-"*20)
    print(data["docs"][1])

    name_film: str = data_film['name']
    names_film: str = data_film['names']

    rating_kp_film = data_film['rating']['kp']
    rating_imdb_film = data_film['rating']['imdb']
    age_rating_film = data_film.get('ageRating')
    poster_film = data_film['poster']['url']
    description_film = data_film['description']
    type_film = data_film['type']
    year_film = data_film['year']
    countries_film = data_film['countries'][0]['name']
    # persons_film: Dict[str, List[Person]] = get_info_person(data)
    # print(persons_film)

    print('Название:', name_film)
    print("Рейтинг КП:", rating_kp_film, "Рейтинг IMDB:", rating_imdb_film)
    print("Год производства:", year_film)
    # print("Режиссер:", ','.join(persons_film["director"]))
    print("Страна:", countries_film)
    print("Возрастное ограничение:", age_rating_film)
    print("Жанр:", type_film)
    print("Жанр:", get_info_genres(data))
    print("Постер:", poster_film)
    print("Краткое содержание:", description_film)
