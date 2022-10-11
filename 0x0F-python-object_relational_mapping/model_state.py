#!/usr/bin/python3
"""Python script that uses the module `SQLAlchemy`.

Contains a class definition of a `State` that links to
the MySQL table states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Links to the MySQL table `states`.

    Args:
        __table__name (str): name of MySQL table to link to.
        id (Column): Primary key of the states table.
        name (Column): name column that can't be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
