# coding=utf-8

"""
Module RabbitMQ
"""

import os
import logging

from pika import (
    URLParameters,
    BlockingConnection
)


class UpyRabbitMQ(object):
    """UpyRabbitMQ
    """

    def __init__(self, url=None):
        """Constructor
        """
        try:
            from dotenv import load_dotenv
            load_dotenv()
        except Exception as error:
            logging.error(error)

        if url:
            self.rabbitmq_url = url
        else:
            self.rabbitmq_url = os.environ.get("RABBITMQ_URL")

    def channel_initialize(self):
        """Channel Initialize
        """
        params = URLParameters(self.rabbitmq_url)
        connection = BlockingConnection(params)

        return connection.channel()

    def search_queue(self, key: str, exchange: str = "amq.direct") -> dict:
        """Search Queue
        """
        try:
            channel = self.channel_initialize()

            response = channel.queue_bind(queue=key, exchange=exchange)
            return {
                "status": 200,
                "message": "ok",
                "quantity": response.channel_number
            }
        except Exception as error:
            return {
                "status": error.args[0],
                "message": error.args[1],
                "quantity": 0
            }
