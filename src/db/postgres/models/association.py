from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import MapperProperty, relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import Uuid  # или UUID из postgresql, если нужно
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from src.db.postgres.models.base import Base  # или src.db.postgres.base, как у тебя

wishlist_gift_association = Table(
    "wishlist_gifts",
    Base.metadata,
    Column(
        "wishlist_id",
        PG_UUID(as_uuid=True),               # или Uuid, если не PostgreSQL
        ForeignKey("wishlist.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "gift_id",
        PG_UUID(as_uuid=True),
        ForeignKey("gift.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)