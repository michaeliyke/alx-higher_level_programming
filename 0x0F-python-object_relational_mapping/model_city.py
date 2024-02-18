#!/usr/bin/python3
"""Model city module"""
import sys
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy import (create_engine)
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Class to model the cities table in the database"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
