#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}")

    Session = sessionmaker(bind=engine)
    session = Session()

    state_city = session.query(State, City).filter(
        State.id == City.state.id).all()

    for state, city in state_city:
        print(f"{state.name}: ({city.id}) {city.name}")
