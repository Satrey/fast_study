from sqlalchemy import Text, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base
from database.mixins.id_mixin import IDMixin
from database.mixins.timestamp_mixins import TimestampsMixin


class User(IDMixin, TimestampsMixin, Base):
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(Text, unique=False, nullable=False)
    is_active: Mapped[Boolean] = mapped_column(Boolean, default=False, nullable=False)
    is_superuser: Mapped[Boolean] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[Boolean] = mapped_column(Boolean, default=False, nullable=False)
