#!/usr/bin/python3
"""
 script that prints the first State object from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    # ./9-model_state_filter_a.py michael aka hbtn_0e_4_usa

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        if state.name.find("a") != -1:
            print("{}: {}".format(state.id, state.name))
    session.close()
