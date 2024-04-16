#!/usr/bin/python3
""" Deletes every state containing the letter 'a' """
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def main():
    """ main func """
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains('a'))

    if states:
        for state in states:
            session.delete(state)
    session.commit()


if __name__ == "__main__":
    main()
