import json
from typing import List, Dict, Tuple, Union
import requests

from settings import SiteSettings

site = SiteSettings()


def info_city(name_city: str) -> Tuple:
    """Поиск dest_ids указанного города"""
    url = "https://apidojo-booking-v1.p.rapidapi.com/locations/auto-complete"
    headers = {
        "X-RapidAPI-Key": site.api_key.get_secret_value(),
        "X-RapidAPI-Host": site.host_api
    }
    try:
        text_querystring = {"languagecode": "ru"}
        text_querystring["text"] = name_city

        response = requests.get(url, headers=headers, params=text_querystring)

        date = json.loads(response.text)

    except:
        return (None, None, None)

    if len(date) == 0:
        return (None, None, None)

    if len(date) == 1 and date[0]['city_ufi'] is None:
        return (date[0]['city_name'], date[0]['country'], 0)

    if date[0]['city_ufi']:
        return (date[0]['city_name'], date[0]['country'], date[0]['city_ufi'])
    return (date[1]['city_name'], date[1]['country'], date[1]['city_ufi'])


if __name__ == "__main__":
    city_name, country, city_ufi = info_city('Moscow')
