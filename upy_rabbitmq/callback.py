# coding=utf-8

"""
Module Callback
"""

import logging

from abc import ABC, abstractmethod
from pika import BlockingConnection
from pika.spec import Basic, BasicProperties


class CallbackProcess(ABC):
    """CallbackProcess
    """

    def __init__(
            self,
            channel: BlockingConnection,
            method: Basic.Deliver,
            properties: BasicProperties,
            body: bytes):
        """Base Constructor
        """
        self.channel = channel
        self.method = method
        self.properties = properties
        self.body = body

        self.run()

    @abstractmethod
    def process(self):
        """Process
        """
        logging.warning(self.body)

    def run(self):
        """Execution
        """
        logging.warning("Execution")

        try:
            self.process()
        except Exception as error:
            logging.error(error)

        finally:
            self.channel.basic_ack(
                delivery_tag=self.method.delivery_tag
            )
