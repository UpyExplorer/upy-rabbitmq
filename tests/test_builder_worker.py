from upy_rabbitmq.builder import WorkerBuilder


def test_client_builder_debug_true():
    client = WorkerBuilder(
        connection=None, 
        debug=True
    )
    assert isinstance(client, WorkerBuilder)


def test_client_builder_debug_true_start_queue():
    client = WorkerBuilder(
        connection=None, 
        debug=True
    )
    assert client.start_queue() is True
