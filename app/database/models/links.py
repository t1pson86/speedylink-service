from sqlalchemy.orm import Mapped, mapped_column

from ..db import Base

class LinksModel(Base):
    __tablename__ = 'links'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    long_name: Mapped[str] = mapped_column(nullable=False)
    short_name: Mapped[str] = mapped_column(nullable=True)