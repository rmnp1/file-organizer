FROM python:3.14-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD . /app

WORKDIR /app

RUN uv sync --locked

ENV TARGET_DIR=/data

CMD ["uv", "run", "main.py"]