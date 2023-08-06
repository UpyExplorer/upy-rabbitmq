import os
import sys
import time
import logging

from upy_rabbitmq.callback import CallbackProcess
from main import worker


class MyCallBack(CallbackProcess):

    def process(self):
        time.sleep(5)
        logging.warning(self.body)


def main():
    worker.start_queue(
        key="key",
        callback=MyCallBack
    )


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.error("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
