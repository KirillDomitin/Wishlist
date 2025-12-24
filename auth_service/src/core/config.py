#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from logging import config as logging_config

from .logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = os.getenv('DEBUG') == 1
    user: str = os.getenv("POSTGRES_USER", 'postgres')
    password: str = os.getenv("POSTGRES_PASSWORD", '123')
    postgres_host: str = os.getenv("POSTGRES_HOST", 'localhost')
    postgres_port: str = os.getenv("POSTGRES_PORT", '5430')
    db_name: str = os.getenv("POSTGRES_DB", 'wishlist_db')
    dsn: str = f'postgresql+psycopg://{user}:{password}@{postgres_host}:{postgres_port}/{db_name}'

    PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'Wishlist API')
    # Корень проекта
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Здесь потом добавим SECRET_KEY, JWT и т.д.


settings = Settings()
