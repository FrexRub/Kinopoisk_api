import asyncio
import json

from utils import get_movie_id
from messages import message_err, message_no_id, message_info_film


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    adata, code = asyncio.run(get_movie_id(id=str(666)))
    # adata, code = asyncio.run(get_movie_id(id=str(4647040)))

    # with open('json_data.json', 'r') as file:
    #     adata = json.load(file)
    # code = 200

    if code != 200:
        asyncio.run(message_err(code))
    elif adata.get("id") is None:
        asyncio.run(message_no_id())
    else:
        asyncio.run(message_info_film(adata))