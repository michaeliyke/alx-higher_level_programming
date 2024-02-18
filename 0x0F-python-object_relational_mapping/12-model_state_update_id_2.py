#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine, collate
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    # ./11-model_state_insert.py michael aka hbtn_0e_4_usa

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = State(name="Louisiana")
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
