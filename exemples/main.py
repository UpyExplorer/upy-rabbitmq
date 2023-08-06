from upy_rabbitmq.builder import UpyRabbitMQ


config = {
    "username": "guest",
    "password": "guest",
    "host": "localhost",
    "port": 5672
}

rabbit_mq = UpyRabbitMQ(
    config=config, 
    debug=False
)

worker = rabbit_mq.new_worker()
client = rabbit_mq.new_client()
