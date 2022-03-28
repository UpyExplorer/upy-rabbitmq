# upy-rabbitmq

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/upy-rabbitmq)
![PyPI - License](https://img.shields.io/pypi/l/upy-rabbitmq)
![PyPI](https://img.shields.io/pypi/v/upy-rabbitmq)
![GitHub last commit](https://img.shields.io/github/last-commit/UpyExplorer/upy-rabbitmq)
![GitHub followers](https://img.shields.io/github/followers/UpyExplorer?label=UpyExplorer&style=social)
<br>

## How to install?
```python

pip install upy-rabbitmq

```
<!-- CONFIG -->
## Config

Add an environment variation called **RABBITMQ_URL** in your project's .env file.

```

RABBITMQ_URL=amqp://user:password@remote.server.com:port//vhost

```
## Start Queue

```python

from upy_rabbitmq.worker import UpyMQWorker

worker = UpyMQWorker()
worker.start_queue(
    key="key",
    callback=callback
)
```
## New Task

```python

from upy_rabbitmq.worker import UpyMQClient

client = UpyMQClient()
client.new_task(
    key="key",
    message="Hello"
)
```
<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Fernando Celmer- email@fernandocelmer.com

Project Link: [https://github.com/UpyExplorer/upy-rabbitmq](https://github.com/UpyExplorer/upy-rabbitmq)
