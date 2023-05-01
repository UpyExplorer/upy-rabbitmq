# coding=utf-8

"""
Module Callback
"""

import logging


class CallbackProcess(object):
    """CallbackProcess
    """
    process_type = 'callback'

    def __init__(self, channel, method, properties, body):
        """Base Constructor 
        """
        self.channel = channel
        self.method = method
        self.properties = properties
        self.body = body

        self.run()

    def process(self):
        """Process
        """
        logging.info("Process")

    def run(self):
        """Execution
        """
        logging.info("Execution")

        try:
            self.process()
        except Exception as error:
            logging.error(error)

        finally:
            self.channel.basic_ack(
                delivery_tag=self.method.delivery_tag
            )
