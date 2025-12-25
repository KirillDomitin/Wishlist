#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis
from src.core.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL)