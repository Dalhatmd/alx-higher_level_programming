#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def main():
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.id, State.name)\
        .order_by(State.id)\
        .filter(State.name.like('%a')).all()

    for i, state in query:
        print(f"{i}: {state}")


if __name__ == "__main__":
    main()
