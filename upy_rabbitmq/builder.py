import os
import pika

from time import time
from rich import print
from dotenv import load_dotenv
from pydantic import BaseModel, Field


def print_debug(name: str):
    print(f"[bold yellow]Warning[/bold yellow]: '{name}' executed in debug mode.")


class SchemaURI(BaseModel):

    username: str = Field(default='username')
    password: str = Field(default='password')
    host: str = Field(default='localhost')
    port: int = Field(default=5672)


class Client:

    def __init__(self, connection) -> None:
        self.connection = connection

    def new_task(self, key: str, message: str, exchange: str = "", max_retries: int = 1):
        timestamp = int(time())
        headers = {
            'max_retries': max_retries,
            'created': timestamp
        }

        properties = pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
                priority=0,
                timestamp=timestamp,
                headers=headers
		    )

        self.connection.queue_declare(queue=key, durable=True)
        self.connection.basic_publish(
            exchange=exchange,
            routing_key=key,
            body=message,
            properties=properties
        )
        self.connection.close()


class ClientBuilder:

    def __new__(cls, connection: object, debug: bool):
        if debug:
            return super(ClientBuilder, cls).__new__(cls)
        else:
            return Client(connection=connection)

    def new_task(self, *args, **kwargs) -> bool:
        print_debug(name="new_task")
        return True


class Worker:

    def __init__(self, connection) -> None:
        self.connection = connection

    def start_queue(self, key: str, callback: object):
        self.connection.queue_declare(queue=key, durable=True)
        self.connection.basic_qos(prefetch_count=1)
        self.connection.basic_consume(queue=key, on_message_callback=callback)
        self.connection.start_consuming()


class WorkerBuilder:

    def __new__(cls, debug: bool, connection: object):
        if debug:
            return super(WorkerBuilder, cls).__new__(cls)
        else:
            return Worker(connection=connection)

    def start_queue(self, *args, **kwargs) -> bool:
        print_debug(name="start_queue")
        return True


class UpyRabbitMQ:

    def __init__(self, config: dict = {}, debug: bool = False) -> None:
        self.config = config
        self.debug = debug

        self.uri = self._get_uri()
        self.connection = self._get_connection()

    def _get_uri(self):
        if self.config:
            uri = SchemaURI(**self.config)
            return f"amqp://{uri.username}:{uri.password}@{uri.host}:{uri.port}"
        else:
            load_dotenv()
            return os.getenv("RABBITMQ_URL") or os.getenv("RABBITMQ_URI")

    def _get_connection(self):
        if self.debug:
            return None
        else:
            params = pika.URLParameters(self.uri)
            return pika.BlockingConnection(params).channel()

    def new_client(self):
        connection = self._get_connection()
        self.client = ClientBuilder(
            connection=connection,
            debug=self.debug
        )
        return self.client

    def new_worker(self):
        connection = self._get_connection()
        self.worker = WorkerBuilder(
            connection=connection,
            debug=self.debug
        )
        return self.worker
