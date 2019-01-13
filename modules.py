from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def config_db():
    POSTGRES = {
        'user': 'postgres',
        'pw': '1234',
        'db': 'HRMRPAY',
        'host': 'localhost',
        'port': '5432'}
    return POSTGRES



class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destinition = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)