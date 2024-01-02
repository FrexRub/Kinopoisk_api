import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)


class SiteSettings(BaseSettings):
    api_key: SecretStr = os.getenv("SITE_API", None)
    # host_api: StrictStr = os.getenv("HOST_API", None)


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "logfile.log",
            "mode": "a"
        }
    },
    "loggers": {
        "utils": {
            "level": "DEBUG",
            "handlers": ["file"],
            # "handlers": ["console", "file"],
            "propagate": False,
        },
        "messages": {
            "level": "DEBUG",
            "handlers": ["file"],
            # "handlers": ["console", "file"],
            "propagate": False,
        }
    }
}
