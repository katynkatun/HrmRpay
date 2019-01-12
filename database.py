import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:1234@localhost:5432/HRMRPAY')
db = scoped_session(sessionmaker(bind = engine))

def main():
    flights = db.execute("SELECT * from flights").fetchall()
    for flight in flights:
        print (flight)

if __name__ == "__main__":
    main()