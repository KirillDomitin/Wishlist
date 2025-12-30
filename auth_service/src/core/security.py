#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid
from datetime import timedelta, datetime, UTC

import bcrypt
import jwt
from db.redis.redis import redis_client
from db.postgres.session import get_db
from .config import settings


def get_password_hash(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    payload = data.copy()
    now = datetime.now(UTC)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=settings.access_token_expire_minutes)
    payload.update({
        "exp": expire,
        "jti": str(uuid.uuid4()),  # уникальный ID токена
        "type": "access"
    })
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def create_refresh_token(data: dict, expires_delta: timedelta | None = None) -> str:
    payload = data.copy()
    now = datetime.now(UTC)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(hours=settings.refresh_token_expire_hours)
    payload.update({
        "exp": expire,
        "jti": str(uuid.uuid4()),  # уникальный ID токена
        "type": "refresh"
    })
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


async def blacklist_token(jti: str, expires_in: int):
    await redis_client.setex(jti, expires_in, "revoked")


async def is_token_blacklisted(jti: str) -> bool:
    return await redis_client.exists(jti)
