#!/usr/bin/python
# -*- coding: utf-8 -*-

from fastapi import FastAPI

from api.v1.router import api_router
from core.config import settings

app = FastAPI(
    # Конфигурируем название проекта. Оно будет отображаться в документации
    title=settings.PROJECT_NAME,
    description="лёгкий сервис, отвечает только за аутентификацию. "
                "Поддержка JWT (access и rearesh токены).",
    version="0.1.0",
    docs_url="/docs",  # Swagger UI
    redoc_url = "/redoc",  # ReDoc (опционально, но удобно)
    #default_response_class=ORJSONResponse, # В проде раскомментировать
)

# Подключаем все роутеры версии 1
app.include_router(api_router, prefix="/api/v1")


# Простой health check на корне
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API работает!"}
