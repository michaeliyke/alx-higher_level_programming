#!/usr/bin/python3
"""script that prints all City objects from the database"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv
    from model_city import City

    # ./14-model_city_fetch_by_state.py michael aka hbtn_0e_4_usa

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    city = City(name="San Francisco", state=State(name="California"))
    session.add(city)
    session.commit()
    session.close()
