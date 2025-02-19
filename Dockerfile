FROM python:3.10.4-slim

ENV POETRY_VERSION=1.5.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /opt/app

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root --no-dev

COPY ./skymarket/. .

COPY .env .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
