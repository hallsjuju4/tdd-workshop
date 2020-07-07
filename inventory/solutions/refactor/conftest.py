from . inventory import Inventory

import pytest

@pytest.fixture
def default_inv():
    return Inventory()

@pytest.fixture
def ten_pants_inv():
    inv = Inventory()
    inv.set_stock('Pants', 50.00, 10)
    return inv
