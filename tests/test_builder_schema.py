import json
import pytest

from pydantic import ValidationError

from tests.conftest import data_uri
from upy_rabbitmq.builder import SchemaURI



def test_builder_schema_success_instace(data_uri):
    data = data_uri.copy()
    schema = SchemaURI(**data)

    assert schema.username == "guest"
    assert schema.password == "guest"
    assert schema.host == "localhost"
    assert schema.port == 5672


def test_builder_schema_success_uri(data_uri):
    data = data_uri.copy()
    schema = SchemaURI(**data)

    assert schema.uri == 'amqp://guest:guest@localhost:5672'


def test_builder_schema_error_string_type(data_uri):
    data = data_uri.copy()
    data["username"] = False

    with pytest.raises(ValidationError) as error:
        SchemaURI(**data)
    output = json.loads(error.value.json())

    assert output[0]["type"] == "string_type"
    assert output[0]["loc"][0] == "username"


def test_builder_schema_error_int_parsing(data_uri):
    data = data_uri.copy()
    data["port"] = "False"

    with pytest.raises(ValidationError) as error:
        SchemaURI(**data)
    output = json.loads(error.value.json())

    assert output[0]["type"] == "int_parsing"
    assert output[0]["loc"][0] == "port"
