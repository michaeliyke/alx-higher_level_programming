#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the
letter a from the database
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    # ./13-model_state_delete_a.py michael aka hbtn_0e_4_usa
    # ./7-model_state_fetch_all.py michael aka hbtn_0e_4_usa

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = session.query(State).filter(State.name.like('%a%'))
    query.delete()

    session.commit()
    session.close()
