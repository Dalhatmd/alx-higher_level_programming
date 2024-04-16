#!/usr/bin/python3
""" Disolays an input search state"""
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

    search_state = (session.query(State.id)
                    .filter(State.name.like
                            (f"%{argv[4]}")).scalar())

    if search_state:
        print(search_state)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
