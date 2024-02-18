#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    # ./7-model_state_fetch_all.py michael aka hbtn_0e_6_usa

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
