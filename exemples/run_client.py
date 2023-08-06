import logging

from main import client


def main():
    client.new_task(
        key="key",
        message="Hello"
    )


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        logging.error(error)
