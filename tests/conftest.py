import pytest


@pytest.fixture
def data_uri():
    return {
        "username": "guest",
        "password": "guest",
        "host": "localhost",
        "port": 5672
    }
