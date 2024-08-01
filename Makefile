lint:
	@poetry run flake8 gendiff

test:
	@poetry run pytest

install:
	@poetry install

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
