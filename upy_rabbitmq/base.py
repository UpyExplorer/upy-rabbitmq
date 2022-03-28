# coding=utf-8

"""
Module RabbitMQ
"""

import os
import pika

class UpyRabbitMQ(object):
    """UpyRabbitMQ
    """

    def __init__(self, url=None):
        """Constructor
        """
        if url:
            self.rabbitmq_url = url
        else:
            self.rabbitmq_url = os.environ.get("RABBITMQ_URL")

    def channel_initialize(self):
        """Channel Initialize
        """
        params = pika.URLParameters(self.rabbitmq_url)
        connection = pika.BlockingConnection(params)

        return connection.channel()

    def search_queue(self, key, exchange=None):
        """Search Queue
        """
        exchange = exchange or "amq.direct"

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
