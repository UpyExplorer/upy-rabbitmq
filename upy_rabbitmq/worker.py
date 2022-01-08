# coding=utf-8

"""
Module Worker
"""

from upy_rabbitmq.base import UpyRabbitMQ

class UpyMQWorker(UpyRabbitMQ):
    """Class responsible for orchestrating and initiating work processes
    """

    def start_queue(self, key, callback):
        """Start Queue
        """
        channel = self.channel_initialize()

        channel.queue_declare(queue=key, durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=key, on_message_callback=callback)
        channel.start_consuming()
