ARG BUILD_TIME_PYTHONBUFFERED=1


# BASE STAGE
FROM python:3.12.2-slim AS base

ARG BUILD_TIME_PYTHONBUFFERED
ENV POETRY_VERSION=1.7.1 \
        PYTHONBUFFERED=$BUILD_TIME_PYTHONBUFFERED

RUN pip3 install "poetry==$POETRY_VERSION"


# DEVELOPMENT STAGE
FROM base AS development

WORKDIR /app

COPY . .

RUN poetry lock --no-update
RUN poetry install

EXPOSE 8080

CMD ["poetry", "run", "run_app"]


# PREPARE WHEELS FOR PRODUCTION STAGE
FROM base AS prepare_production

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY ./src ./src
RUN poetry lock --no-update
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt


# PRODUCTION STAGE
FROM python:3.12.2-slim AS production

ARG BUILD_TIME_PYTHONBUFFERED
ENV  PYTHONBUFFERED=$BUILD_TIME_PYTHONBUFFERED

WORKDIR /app

COPY --from=prepare_production /app/requirements.txt ./
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

COPY ./src ./src
COPY ./alembic.ini .
COPY ./alembic ./alembic
COPY ./start.sh .

RUN chmod +x start.sh

EXPOSE 80
CMD ["./start.sh"]
