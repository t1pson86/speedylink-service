from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from ..db import Base

class LinksModel(Base):
    __tablename__ = 'links'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    long_url: Mapped[str] = mapped_column(nullable=False)
    short_url: Mapped[str] = mapped_column(nullable=True, default=None)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["UsersModel"] = relationship(back_populates="links")