FROM python:3.9

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.1.10

RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /project
COPY poetry.lock pyproject.toml /project/

# Project initialization:
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Creating folders, and files for a pyproject:
COPY . /project/