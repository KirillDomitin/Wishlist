#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.api.v1.users.router import router as user_router
from fastapi import APIRouter
api_router = APIRouter()

api_router.include_router(user_router, prefix="/users", tags=["users"])