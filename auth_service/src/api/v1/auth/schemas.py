#!/usr/bin/python
# -*- coding: utf-8 -*-

from pydantic import BaseModel

class Token(BaseModel):
    access: str
    refresh: str

class Login(BaseModel):
    email: str
    password: str