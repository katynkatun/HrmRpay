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
    __tablename = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Passenger(db.Model):
    __tablename__ = "passengers"
    name = db.Column(db.String, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)