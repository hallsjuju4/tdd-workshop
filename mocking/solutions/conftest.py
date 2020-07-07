from .fake_server import inv_server as mocked_server

import pytest


@pytest.fixture(scope="session", autouse=True)
def start_server():
    mocked_server.run_bg()
