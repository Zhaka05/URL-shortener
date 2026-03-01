from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class ShortUrl(Base):
    __tablename__ = "short_urls"
    id = Column(Integer, primary_key=True, autoincrement=True)

    slug: Mapped[str] = mapped_column(primary_key=True)
    long_url: Mapped[str]