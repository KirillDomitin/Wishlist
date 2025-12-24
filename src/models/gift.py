#!/usr/bin/python
# -*- coding: utf-8 -*-
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import String, Text, Boolean, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .association import wishlist_gift_association
from .base import Base
from .common import TimeStampedMixin, uuid_pk

if TYPE_CHECKING:
    from .wishlist import Wishlist




class Gift(Base, TimeStampedMixin):
    __tablename__ = "gift"

    id: Mapped[uuid_pk]

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    url: Mapped[str | None] = mapped_column(String(512), nullable=True)
    image_url: Mapped[str | None] = mapped_column(String(512), nullable=True)

    price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    currency: Mapped[str] = mapped_column(String(3), default="RUB", nullable=False)

    is_reserved: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    wishlists: Mapped[list["Wishlist"]] = relationship(
        "Wishlist",
        secondary=wishlist_gift_association,
        back_populates="gifts",
    )
