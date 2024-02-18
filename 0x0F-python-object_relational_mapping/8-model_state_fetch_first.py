#!/usr/bin/python3
"""
 script that prints the first State object from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    # ./8-model_state_fetch_first.py michael aka hbtn_0e_4_usa

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
