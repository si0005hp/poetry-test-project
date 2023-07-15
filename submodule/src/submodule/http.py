import requests


def get(url: str) -> requests.models.Response:
    return requests.get(url)
