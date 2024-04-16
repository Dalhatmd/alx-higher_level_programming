#!/usr/bin/python3
""" Add new state to database table """
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def main():
    """ main func"""
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    query = session.query(State.id).filter(State.name.like(
        "Lousiana")).scalar()
    print(query)


if __name__ == "__main__":
    main()
