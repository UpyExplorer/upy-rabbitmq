# coding=utf-8

"""
Module Client
"""

import pika
from upy_rabbitmq.base import UpyRabbitMQ


class UpyMQClient(UpyRabbitMQ):
    """Class responsible for producing new messages
    """

    def new_task(self, key: str, message: str, exchange: str = ""):
        """New Task
        """
        channel = self.channel_initialize()

        channel.queue_declare(queue=key, durable=True)
        channel.basic_publish(
            exchange=exchange,
            routing_key=key,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
