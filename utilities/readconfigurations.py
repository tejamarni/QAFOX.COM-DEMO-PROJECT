from configparser import ConfigParser
from pathlib import Path


def read_configuration(category: str, key: str) -> str:
    config = ConfigParser()
    config_file = Path(__file__).resolve().parent.parent / "configurations" / "config.ini"
    config.read(config_file)
    return config.get(category, key)
