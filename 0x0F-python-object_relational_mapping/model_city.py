#!/usr/bin/python3
# model state
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    class State
    """

    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement="auto"
        )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
