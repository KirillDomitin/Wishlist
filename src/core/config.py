#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from logging import config as logging_config

from .logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)

# # Название проекта. Используется в Swagger-документации
# PROJECT_NAME = os.getenv('PROJECT_NAME', 'Wishlist')
#
# # Настройки Redis
# REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
# REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
#
# # Настройки Elasticsearch
# ELASTIC_HOST = os.getenv('ELASTIC_HOST', '127.0.0.1')
# ELASTIC_PORT = int(os.getenv('ELASTIC_PORT', 9200))
#
# # Корень проекта
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = os.getenv('DEBUG') == 1
    user: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    postgres_host: str = os.getenv("POSTGRES_HOST")
    postgres_port: str = os.getenv("POSTGRES_PORT")
    db_name: str = os.getenv("POSTGRES_DB")
    dsn: str = f'postgresql+psycopg://{user}:{password}@{postgres_host}:{postgres_port}/{db_name}'

    PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'Wishlist')
    # Корень проекта
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Здесь потом добавим SECRET_KEY, JWT и т.д.


settings = Settings()
