## Описание

Этот проект представляет собой утилиту для сравнения конфигурационных файлов .json и .yaml/yml. Он поддерживает различные форматы вывода, включая "stylish", "plain" и "json". Программа позволяет легко выявлять различия между двумя конфигурационными файлами, предоставляя удобное и понятное отображение различий.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/JoeCapHuang/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/JoeCapHuang/python-project-50/actions)
[![pyci](https://github.com/JoeCapHuang/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/JoeCapHuang/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/0ed8dcb4c6d528a22d57/maintainability)](https://codeclimate.com/github/JoeCapHuang/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/0ed8dcb4c6d528a22d57/test_coverage)](https://codeclimate.com/github/JoeCapHuang/python-project-50/test_coverage)

## Установка

1. Клонируйте репозиторий на ваше локальное устройство:
    ```bash
    git clone https://github.com/JoeCapHuang/python-project-50.git
    ```

2. Перейдите в директорию проекта

3. Убедитесь, что у вас установлен [Poetry](https://python-poetry.org/docs/). Если нет, установите его с помощью следующей команды:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

4. Установите все необходимые зависимости с помощью Poetry:
    ```bash
    poetry install
    ```

5. Сборка билда:
    ```bash
    poetry build
    ```

6. Установка билда:
    ```bash
    python3 -m pip install --user dist/*.whl
    ```

## Примеры работы программы:
[![asciicast](https://asciinema.org/a/TIvVEHdsDHt19EGQNDsYxmitj.svg)](https://asciinema.org/a/TIvVEHdsDHt19EGQNDsYxmitj)
[![asciicast](https://asciinema.org/a/VSbtelCtHGKJLj6tVIIp3sRbO.svg)](https://asciinema.org/a/VSbtelCtHGKJLj6tVIIp3sRbO)
[![asciicast](https://asciinema.org/a/PXjeLzrmlY6GuQlPrjZABfkrG.svg)](https://asciinema.org/a/PXjeLzrmlY6GuQlPrjZABfkrG)
[![asciicast](https://asciinema.org/a/WXAVk0iCaSkcRdt2gnnt7JoUG.svg)](https://asciinema.org/a/WXAVk0iCaSkcRdt2gnnt7JoUG)
[![asciicast](https://asciinema.org/a/HfVsdJ7Q7GaPPw5zKOxySesOl.svg)](https://asciinema.org/a/HfVsdJ7Q7GaPPw5zKOxySesOl)