setup:
	uv sync

run:
	uv run python manage.py runserver 0.0.0.0:8000

migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate

createsuperuser:
	uv run python manage.py createsuperuser

format:
	uv run ruff check . --fix

lint:
	uv run ruff check .

