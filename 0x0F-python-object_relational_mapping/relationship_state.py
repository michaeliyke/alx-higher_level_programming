#!/usr/bin/python3
"""Model state module"""
import sys
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (create_engine)

Base = declarative_base()


class State(Base):
    """Class to model the states table in the database"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
