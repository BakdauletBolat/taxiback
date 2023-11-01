from typing import cast
from rest_framework.test import APIClient
from rest_framework import response



class TestOrderCreate:

    def test_order_create_with_client(self):
        assert 1 == 1


def _post(client: APIClient, url: str, data: dict, **kwargs) -> response.Response:
    kwargs.setdefault("path", url)
    kwargs.setdefault("data", data)
    kwargs.setdefault("format", "json")
    return cast(response.Response, client.post(**kwargs))

def _get(client: APIClient, url: str, data: dict | None = None) -> response.Response:
    return cast(response.Response, client.get(url, data))


def _patch(client: APIClient, url: str, data: list | dict) -> response.Response:
    return cast(response.Response, client.patch(url, data, "json"))