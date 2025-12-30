#!/usr/bin/python
# -*- coding: utf-8 -*-

from fastapi import APIRouter

from ..v1.auth.router import router as auth_router
from ..v1.users.router import router as user_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(user_router, prefix="/users", tags=["users"])
