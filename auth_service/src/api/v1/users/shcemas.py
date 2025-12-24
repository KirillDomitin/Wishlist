#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, SecretStr, ConfigDict


class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr = Field(description="Email адрес")
    password: SecretStr = Field(
        min_length=8,
        max_length=72,
        description="Пароль минимум 8 символов",
        examples=["StrongPass123!"]
        )
    full_name: str | None = None


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: EmailStr
    full_name: str | None
    is_active: bool
    created_at: datetime
