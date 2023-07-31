#!/usr/bin/python3
"""script that changes the name of a State from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == '__main__':

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}")

    Session = sessionmaker(bind=engine)
    session = Session()

    state_updated = session.query(State).filter(State.id == 2).first()

    if state_updated:
        state_updated.name = 'New Mexico'
        session.commit()
