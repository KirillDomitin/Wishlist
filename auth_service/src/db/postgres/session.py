#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from core.config import settings

engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,
    pool_size=20,          # мин. соединений в пуле
    max_overflow=10,       # сколько можно превысить
    pool_timeout=30,       # таймаут на получение соединения
    pool_pre_ping=True,    # проверка живости соединения
    pool_recycle=3600,     # переподключение каждые N секунд (защита от таймаутов)
)

AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
