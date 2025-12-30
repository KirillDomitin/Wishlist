#!/usr/bin/python
# -*- coding: utf-8 -*-

from redis.asyncio import Redis

from core.config import settings

# Глобальный клиент
redis_client: Redis | None = None


async def get_redis() -> Redis:
    if redis_client is None:
        raise RuntimeError("Redis client not initialized")
    return redis_client


# Функции жизненного цикла для main.py
async def init_redis():
    global redis_client
    redis_client = Redis.from_url(settings.redis_url)


async def close_redis():
    global redis_client
    if redis_client is not None:
        await redis_client.close()
        redis_client = None
