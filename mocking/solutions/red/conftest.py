from .inventory import Inventory


import pytest
from unittest.mock import create_autospec, MagicMock
from http.client import HTTPConnection
import json


@pytest.fixture
def default_inv():
    return Inventory()


@pytest.fixture
def ten_pants_inv():
    inv = Inventory()
    inv.set_stock('Pants', 50.00, 10)
    return inv


@pytest.fixture
def remote_inv_with_pants():
    rsp = MagicMock()
    rsp.status = 200
    rsp.read.return_value = json.dumps({
        'name': 'Pants',
        'price': 50.00,
        'quantity': 10
    })

    client = create_autospec(HTTPConnection)
    client.getresponse.return_value = rsp
    return Inventory(client=client)


@pytest.fixture
def remote_inv_error():
    rsp = MagicMock()
    rsp.status = 404

    client = create_autospec(HTTPConnection)
    client.getresponse.return_value = rsp
    return Inventory(client=client)
