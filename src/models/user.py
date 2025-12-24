from typing import TYPE_CHECKING

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .common import TimeStampedMixin, uuid_pk

# if TYPE_CHECKING:
from .wishlist import Wishlist

class User(Base, TimeStampedMixin):
    __tablename__ = "user"

    id: Mapped[uuid_pk]  # берём готовый UUID primary key

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Обратная связь: один пользователь — много вишлистов
    wishlists: Mapped[list[Wishlist]] = relationship(
        "Wishlist", back_populates="owner", cascade="all, delete-orphan"
    )