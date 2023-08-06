from upy_rabbitmq.builder import ClientBuilder


def test_client_builder_debug_true():
    client = ClientBuilder(
        connection=None, 
        debug=True
    )
    assert isinstance(client, ClientBuilder)


def test_client_builder_debug_true_new_task():
    client = ClientBuilder(
        connection=None, 
        debug=True
    )
    assert client.new_task() is True
