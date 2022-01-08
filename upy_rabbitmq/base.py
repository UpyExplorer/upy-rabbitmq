# coding=utf-8

"""
Module RabbitMQ
"""

import pika


class UpyRabbitMQ(object):
    """UpyRabbitMQ
    """
    process_type = 'rabbitmq'

    def __init__(self, url):
        """Constructor
        """
        self.rabbitmq_url = url

    def channel_initialize(self):
        """Channel Initialize
        """
        params = pika.URLParameters(self.rabbitmq_url)
        connection = pika.BlockingConnection(params)

        return connection.channel()

    def start_queue(self, key, callback):
        """Start Queue
        """
        channel = self.channel_initialize()

        channel.queue_declare(queue=key, durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=key, on_message_callback=callback)
        channel.start_consuming()
        
    def new_task(self, key, message, exchange=None):
        """New Task
        """
        exchange = exchange or ""
        channel = self.channel_initialize()

        channel.queue_declare(queue=key, durable=True)
        channel.basic_publish(
            exchange=exchange,
            routing_key=key,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        
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
