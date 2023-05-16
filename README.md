# upy-rabbitmq

![GitHub Org's stars](https://img.shields.io/github/stars/UpyExplorer?label=LinuxProfile&style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/upy-rabbitmq)
![PyPI - License](https://img.shields.io/pypi/l/upy-rabbitmq)
![PyPI](https://img.shields.io/pypi/v/upy-rabbitmq)
![GitHub last commit](https://img.shields.io/github/last-commit/UpyExplorer/upy-rabbitmq)

---

- **Documentation**: [https://github.com/UpyExplorer/upy-rabbitmq](https://github.com/UpyExplorer/upy-rabbitmq)
- **Source Code**: [https://github.com/UpyExplorer/upy-rabbitmq](https://github.com/UpyExplorer/upy-rabbitmq)

---

## How to install?

```python
pip install upy-rabbitmq
```

## Config

Add an environment variation called **RABBITMQ_URL** in your project's .env file.

```
RABBITMQ_URL=amqp://user:password@remote.server.com:port//vhost
```

## Callback Class
> callback.py

```python

import time
from upy_rabbitmq.callback import CallbackProcess

class MyCallBack(CallbackProcess):

    def process(self):
        time.sleep(5)
        print(self.body.decode())
```

## Start Queue
> worker.py

```python

from upy_rabbitmq.worker import UpyMQWorker

worker = UpyMQWorker()
worker.start_queue(
    key="key",
    callback=MyCallBack
)
```

## New Task
> client.py

```python
from upy_rabbitmq.client import UpyMQClient

client = UpyMQClient()
client.new_task(
    key="key",
    message="Hello"
)
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Commit Style

- ⚙️ FEATURE
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI
- ❤️️ TEST
- ⬆️ CI/CD
- ⚠️ SECURITY

## License

Distributed under the MIT License. See `LICENSE` for more information.
