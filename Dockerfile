FROM python:3.10 as base

RUN pip install poetry
ENV PATH=$PATH:/root/.local/share/pypoetry/venv/bin/
COPY poetry.lock pyproject.toml /app/
WORKDIR /app
RUN poetry install
COPY todo_app /app/todo_app

FROM base as production
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

FROM base as development
ENTRYPOINT poetry run flask run --host 0.0.0.0

FROM base as test
COPY tests /app/tests
COPY .env.test .env.test
ENTRYPOINT poetry run pytest
