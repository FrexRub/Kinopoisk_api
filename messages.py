from typing import Dict, Any, List, NamedTuple
import logging.config

from settings import dict_config


class Person(NamedTuple):
    id: int
    photo: str
    name: str
    profession: str


def get_info_person(data: Dict[str, Any]) -> Dict[str, List[Person]]:
    """Возвращает информацию по актерам и режиссерам фильма
    :param data: общая информация по фильму
    :type data: Dict[str, Any]

    :return: информация по актерам и режиссерам фильма
    :type: Dict[str, List[Person]]
    """
    persons_film: List[Dict[str, str | int]] = data["persons"]
    dict_persons: Dict[str, List[Person]] = {"actor": [], "director": []}
    for i_dic in persons_film:
        if i_dic["enProfession"] in ("actor", "director"):
            i_person = Person(i_dic["id"], i_dic["photo"],
                              i_dic["name"], i_dic["profession"])
            if i_person.name:
                dict_persons[i_dic["enProfession"]].append(i_person)

    return dict_persons


def get_info_genres(data: Dict[str, Any]) -> str:
    """Возвращает информацию о жанре картины
    :param data: общая информация по фильму
    :type data: Dict[str, Any]

    :return: информация по актерам и режиссерам фильма
    :type: str
    """
    genres_film: List[Dict[str, str]] = data["genres"]
    result_list: List[str] = list()
    for i_data in genres_film:
        result_list.append(i_data["name"])
    return ','.join(result_list)


def message_err(cod_err: int, data: Dict[str, Any]) -> None:
    """Вывод сообщения об ошибке"""
    print(f"Что-то пошло не так: {cod_err}")
    print(data['message'])


def message_no_id() -> None:
    """Вывод сообщения об отсутствие id"""
    print(f"По этому id ничего не найдено!")


def message_info_film(data: Dict[str, Any]) -> None:
    """Вывод полной информации о фильме
    :param data: общая информация по фильму
    :type data: Dict[str, Any]
    """
    data_film: Dict[str, Any] = data
    logger.debug("Вывод полной информации о фильме")
    try:
        name_film: str = data_film.get('name', "Название фильма не указано")
        rating_kp_film = data_film['rating']['kp']
        rating_imdb_film = data_film['rating']['imdb']
        age_rating_film = data_film.get('ageRating', "Возрастной ценз не указан")
        poster_film = data_film['poster']['url']
        description_film = data_film.get('description', "Описание данного фильма отсутствует")
        type_film = data_film.get('type', "Жанр не указан")
        year_film = data_film['year']
        countries_film = data_film['countries'][0]['name']
        if data.get("persons"):
            persons_film: Dict[str, List[Person]] = get_info_person(data)
            director_film = [i_prof.name for i_prof in persons_film["director"]]
            actor_film = [i_prof.name for i_prof in persons_film["actor"]]
        else:
            director_film = actor_film = None
    except Exception as exp:
        logger.exception(exp)
    else:
        print('Название:', name_film)
    print("Рейтинг КП:", rating_kp_film, "Рейтинг IMDB:", rating_imdb_film)
    print("Год производства:", year_film)
    if isinstance(director_film, list):
        try:
            print("Режиссер:", ','.join(director_film))
        except TypeError as exp:
            logger.debug(actor_film)
            logger.exception(exp)
    if isinstance(actor_film, list):
        try:
            fprint(f"Актёры: {','.join(actor_film)}")
        except TypeError as exp:
            logger.debug(actor_film)
            logger.exception(exp)
    print("Страна:", countries_film)
    print("Возрастное ограничение:", age_rating_film)
    print("Жанр:", type_film)
    print("Жанр:", get_info_genres(data))
    print("Постер:", poster_film)
    fprint(f"Краткое содержание: {description_film}")


def message_short_info_film(data: Dict[str, Any]) -> None:
    """Вывод краткой информации о фильме
    :param data: общая информация по фильму
    :type data: Dict[str, Any]
    """
    logger.debug("Вывод краткой информации о фильме")
    data_film: Dict[str, Any] = data
    try:
        name_film: str = data_film.get('name', "отсутствует")
        rating_film = data_film.get('rating', "отсутствует")
        poster_film = data_film.get('poster', "отсутствует")
        description_film = data_film.get('description', "отсутствует")
        type_film = data_film.get('type', "отсутствует")
        year_film = data_film.get('year', "отсутствует")
        countries_film = data_film.get('countries', "отсутствует")
    except Exception as exp:
        logger.exception(exp)
    else:
        print('id:', data_film['id'])
        print('Название:', name_film)
        print("Рейтинг:", rating_film)
        print("Год производства:", year_film)
        print("Страна:", ','.join(countries_film))
        print("Жанр:", type_film)
        if data_film.get("genres"):
            print("Жанр:", ','.join(data_film["genres"]))
        print("Постер:", poster_film)
        fprint(f"Краткое содержание: {description_film}")


def fprint(out_text: str, width: int = 65) -> None:
    """Вывод теска с использованием заданной ширины вывода
    :param out_text: выводимы текст
    :type out_text: str
    :param width: ширина вывода текста
    :type width: int
    """
    try:
        out_text_list: List[str] = [out_text[i_step:width + i_step] for i_step in range(0, len(out_text), width)]
        print('\n'.join(out_text_list))
    except TypeError as exp:
        logger.error(out_text)
        logger.exception(exp)


logging.config.dictConfig(dict_config)
logger = logging.getLogger('messages')

if __name__ in "__main__":
    fprint('1234567890')
