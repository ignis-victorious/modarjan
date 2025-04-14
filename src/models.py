#  ________________
#  Import LIBRARIES
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
#  Import FILES
#  ________________


# SQLAlchemy model
Base = declarative_base()


# Hero - SQLAlchemy
class DBHero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    secret_name = Column(String)
    age = Column(Integer, nullable=True)


# # Hero - SQLModel
class Hero(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str
    secret_name: str
    age: int | None
