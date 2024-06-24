import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db

class Gymnast(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(128), index=True)
    surname: so.Mapped[str] = so.mapped_column(sa.String(128), index=True)
    level: so.Mapped[str] = so.mapped_column(sa.String(32), index=True)
    age_group: so.Mapped[str | None] = so.mapped_column(sa.String(8))
    club: so.Mapped[str] = so.mapped_column(sa.String(64))

    __table_args__ = (sa.UniqueConstraint(name, surname),)

    music: so.Mapped[list["GymnastMusic"]] = so.relationship(back_populates="gymnast")

    def __repr__(self) -> str:
        return f"<Gymnast: {self.name} {self.surname}>"

class GymnastMusic(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    gymnast_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Gymnast.id), index=True)
    apparatus: so.Mapped[str] = so.mapped_column(sa.String(16))
    music_location: so.Mapped[str] = so.mapped_column(sa.String(128))

    gymnast: so.Mapped[Gymnast] = so.relationship(back_populates="music")

    def __repr__(self) -> str:
        return f"<Music file: {self.music_location}"