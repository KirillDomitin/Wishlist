#!/usr/bin/python
# -*- coding: utf-8 -*-
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.v1.router import api_router
from core.config import settings
from db.redis.redis import get_redis, init_redis, close_redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_redis()
    yield
    await close_redis()


app = FastAPI(
    title=settings.project_name,
    description="лёгкий сервис, отвечает только за аутентификацию. "
                "Поддержка JWT (access и rearesh токены).",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
    # default_response_class=ORJSONResponse, # В проде раскомментировать
)

# Подключаем все роутеры версии 1
app.include_router(api_router, prefix="/api/v1")


# Простой health check на корне
@app.get("/redis-health")
async def health_check():
    redis_client = await get_redis()
    return {"redis": "OK" if redis_client.ping() else "NOK"}
