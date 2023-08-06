from tests.conftest import data_uri
from upy_rabbitmq.builder import UpyRabbitMQ


def test_builder_debug_true_data_config(data_uri):
    rabbit_mq = UpyRabbitMQ(config=data_uri, debug=True)

    assert rabbit_mq.config == data_uri
    assert rabbit_mq.debug == True
    assert rabbit_mq.uri == "amqp://guest:guest@localhost:5672"


def test_builder_debug_true_data_env_url(monkeypatch):
    url = "amqp://url:pass@host:5672"

    monkeypatch.setenv("RABBITMQ_URL", url)
    rabbit_mq = UpyRabbitMQ(debug=True)

    assert rabbit_mq.config == {}
    assert rabbit_mq.debug == True
    assert rabbit_mq.uri == url


def test_builder_debug_true_data_env_uri(monkeypatch):
    uri = "amqp://uri:pass@host:5672"

    monkeypatch.setenv("RABBITMQ_URI", uri)
    rabbit_mq = UpyRabbitMQ(debug=True)

    assert rabbit_mq.config == {}
    assert rabbit_mq.debug == True
    assert rabbit_mq.uri == uri
