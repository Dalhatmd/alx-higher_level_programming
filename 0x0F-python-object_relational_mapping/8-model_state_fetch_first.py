#!/usr/bin/python3
""" Script that quesries a database using the sqlalchemy orm"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def main():
    """ selects the first name in the states table"""
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"1: {first_state.name}")
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
