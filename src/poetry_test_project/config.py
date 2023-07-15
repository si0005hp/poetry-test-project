import os
import pkgutil
from typing import Any

from utils import read_parquet_as_list
import yaml


class Config:
    def __init__(self, env: str):
        config = yaml.safe_load(pkgutil.get_data(__name__, "config.yml"))
        self.config: dict = config[env]

        data_path = os.path.join(os.path.dirname(__file__), "data.parquet")
        self.data: list[dict] = read_parquet_as_list(data_path)

    def __getattr__(self, key) -> Any:
        try:
            return self.config[key]
        except KeyError:
            raise AttributeError(f"KeyError: {key}")


if __name__ == "__main__":
    config = Config("development")
    print(config.model_version)
    print(config.data)
