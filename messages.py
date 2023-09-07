from pprint import pprint
from typing import Dict, Any


async def message_err(cod_err: int) -> None:
    """Вывод сообщения об ошибке"""
    print(f"Что-то пошло не так: {cod_err}")


async def message_no_id() -> None:
    """Вывод сообщения об отсутствие id"""
    print(f"По этому id ничего не найдено!")


async def message_info_film(data: Dict[str, Any]) -> None:
    """Вывод сообщения об отсутствие id"""
    data_film: Dict[str, Any] = data["docs"][0]
    name_film:str = data_film['name']
    names_film: str = data_film['names']

    print("name_film:", name_film)
    print("names_film:", *names_film)
