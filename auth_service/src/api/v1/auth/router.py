#!/usr/bin/python
# -*- coding: utf-8 -*-

from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select

from core.security import create_access_token, create_refresh_token, verify_password
from db.postgres.session import get_db
from db.redis.redis import redis_client
from core.security import blacklist_token
from models.user import User
from .schemas import Token

router = APIRouter()


@router.post(
    "/",
    response_model=Token,
    status_code=status.HTTP_200_OK,
    summary="Логин пользователя",
    description="Логин пользователя по email и паролю"
)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db=Depends(get_db),
):
    result = await db.execute(select(User).where(User.email == form_data.username))
    existing_user = result.scalar_one_or_none()
    if not existing_user:
        raise HTTPException(status_code=400, detail="User with email not found")

    hashed_password = existing_user.hashed_password
    if not verify_password(form_data.password, hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")

    access_token = create_access_token(data={"sub": existing_user.email})
    refresh_token = create_refresh_token(data={"sub": existing_user.email})
    return Token(access=access_token, refresh=refresh_token)

@router.post(
    "refresh/",
    response_model=Token,
    status_code=status.HTTP_200_OK,
    summary="Обновление токенов",
    description="Обновление токенов"
)
async def refresh(refresh_jid):
