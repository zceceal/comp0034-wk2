from typing import List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from paralympics import db



class Region(db.Model):
    __tablename__ = "region"
    NOC: Mapped[str] = mapped_column(db.Text, primary_key=True)
    region: Mapped[str] = mapped_column(db.Text, nullable=False)
    notes: Mapped[str] = mapped_column(db.Text, nullable=True)
    events: Mapped[List["Event"]] = relationship(back_populates="region") # PRIMARY KEY TABLE


class Event(db.Model):
    __tablename__ = "event"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    type: Mapped[str] = mapped_column(db.Text, nullable=False)
    year: Mapped[int] = mapped_column(db.Integer, nullable=False)
    country: Mapped[str] = mapped_column(db.Text, nullable=False)
    host: Mapped[str] = mapped_column(db.Text, nullable=False)
    NOC: Mapped[str] = mapped_column(ForeignKey("region.NOC"))
    # add relationship to the parent table, Region, which has a relationship called 'events'
    region: Mapped["Region"] = relationship("Region", back_populates="events") # FOREIGN KEY TABLE
    start: Mapped[str] = mapped_column(db.Text, nullable=True)
    end: Mapped[str] = mapped_column(db.Text, nullable=True)
    duration: Mapped[int] = mapped_column(db.Integer, nullable=True)
    disabilities_included: Mapped[str] = mapped_column(db.Text, nullable=True)
    countries: Mapped[str] = mapped_column(db.Text, nullable=True)
    events: Mapped[int] = mapped_column(db.Integer, nullable=True)
    athletes: Mapped[int] = mapped_column(db.Integer, nullable=True)
    sports: Mapped[int] = mapped_column(db.Integer, nullable=True)
    participants_m: Mapped[int] = mapped_column(db.Integer, nullable=True)
    participants_f: Mapped[int] = mapped_column(db.Integer, nullable=True)
    participants: Mapped[int] = mapped_column(db.Integer, nullable=True)
    highlights: Mapped[str] = mapped_column(db.Text, nullable=True)
    

class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    email: Mapped[str] = mapped_column(db.Text, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.Text, unique=True, nullable=False)

    def __init__(self, email: str, password: str):
        """
        Create a new User object using hashing the plain text password.
        :type password_string: str
        :type email: str
        :returns None
        """
        self.email = email
        self.password = password