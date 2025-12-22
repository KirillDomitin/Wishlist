#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.postgres.models.base import Base
from src.db.postgres.models.common import uuid_pk, TimeStampedMixin
from .association import wishlist_gift_association

if TYPE_CHECKING:
    from .gift import Gift
    from .user import User


class Wishlist(Base, TimeStampedMixin):
    __tablename__ = "wishlist"

    id: Mapped[uuid_pk]

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_public: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False, index=True
    )

    # Уникальный токен для публичной ссылки
    shared_token: Mapped[str | None] = mapped_column(
        String(64),  # secrets.token_urlsafe(32)
        unique=True,
        nullable=True,
        default=None,
        index=True
    )

    # Связь с пользователем (один пользователь — много вишлистов)
    owner_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )

    # обратно к владельцу
    owner: Mapped["User"] = relationship("User", back_populates="wishlist")

    gifts: Mapped[list["Gift"]] = relationship(
        "Gift",
        secondary=wishlist_gift_association,
        back_populates="wishlist",
    )
