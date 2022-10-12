#!/usr/bin/python3
"""Using python module `SQLAlchemy` to list all the State objects."""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import select, create_engine

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    url = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"
    engine = create_engine(url, pool_pre_ping=True)

    stmt = select(State).filter(State.name.contains('a')).\
        order_by(State.id)
    with Session(engine) as session:
        for state in session.scalars(stmt):
            print(f'{state.id}: {state.name}')
