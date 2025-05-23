setup:
	uv pip install -r pyproject.toml
	uv pip install --deps -r pyproject.toml
	uv pip compile pyproject.toml


run:
	uv run python manage.py runserver


migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate

superuser:
	uv run python manage.py createsuperuser


format:
	uv run ruff check . --fix

lint:
	uv run ruff check .

