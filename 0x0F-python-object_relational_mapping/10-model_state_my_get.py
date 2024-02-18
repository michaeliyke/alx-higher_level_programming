#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine, collate
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    # ./10-model_state_my_get.py michael aka hbtn_0e_4_usa Texas

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = session.query(State).order_by(State.id)
    state = query.filter(State.name == argv[4]).first()
    if state and state.name == argv[4]:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
