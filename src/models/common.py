#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid
from datetime import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, mapped_column

# Общие аннотации для переиспользования
uuid_pk = Annotated[
    uuid.UUID,
    mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,  # или uuid.uuid7, если установил uuid6
    ),
]

timestamp = Annotated[datetime, mapped_column(TIMESTAMP(timezone=True))]

class TimeStampedMixin:
    """Миксин с полями created_at и updated_at"""

    created_at: Mapped[timestamp] = mapped_column(
        server_default=func.now(),  # время на стороне БД
        nullable=False,
    )
    updated_at: Mapped[timestamp] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),  # автоматически обновляется при UPDATE
        nullable=False,
    )