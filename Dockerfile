# First stage: Build the base image for Django and Poetry
FROM python:3.11 as python-base

# Environment variable configuration
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE="config.settings.base"

# Working directory
WORKDIR /app

# Copy Poetry configuration files
COPY poetry.lock pyproject.toml /app/

# Install Poetry and project dependencies
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Second stage: Build the image for development
FROM python-base as development-web

# Copy the application source code
COPY . /app/
CMD python manage.py migrate && python manage.py collectstatic --noinput
