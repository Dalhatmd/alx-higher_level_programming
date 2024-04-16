#!/usr/bin/python3
""" doc """
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

    update_state = session.query(State).filter(State.id == 2).first()
    update_state.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    main()
