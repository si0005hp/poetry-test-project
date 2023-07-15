import pkgutil
from typing import Any

import yaml


class Config:
    def __init__(self, env: str):
        data = yaml.safe_load(pkgutil.get_data(__name__, "config.yml"))
        self.config: dict = data[env]

    def __getattr__(self, key) -> Any:
        try:
            return self.config[key]
        except KeyError:
            raise AttributeError(f"KeyError: {key}")


if __name__ == "__main__":
    config = Config("development")
    print(config.model_version)
