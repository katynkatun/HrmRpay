from flask import Flask, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:1234@localhost:5432/HRMRPAY')
db = scoped_session(sessionmaker(bind = engine))

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
@app.route("/main")
def index():
    if (0):
        headLine = 1
    else:
        headLine = 0
    return render_template('index.html', headline = headLine)

@app.route("/listNames")
def listNames():
    listNames = ["Makr", "Bob"]
    return render_template("listNames.html", names = listNames)

@app.route("/formAction")
def formAction():
    return render_template("formAction.html")

@app.route('/hello', methods = ["POST"])
def hello():
    name = request.form.get("name")
    return name

@app.route('/flights')
def flights():
    flights = db.execute("select * from flights").fetchall()
    return render_template("flights.html", flights = flights)

@app.route('/flights/<int:flight_id>')
def flight(flight_id):
    flights = db.execute("select * from flights where id = :id", {"id" : flight_id}).fetchone()
    if flights is None:
        return "Flight not find"
    passengers = db.execute("Select * from passengers where flight_id = :id", {"id" : flight_id}).fetchall()
    return render_template("passengers.html", passengers = passengers)

@app.route('/book', methods =["POST"])
def book():
    name = request.form.get("name")

    if name:
        try:
            flight_id = int(request.form.get('flight_id'))
        except ValueError:
            return "Error"

        if db.execute("SELECT * from flights where id = :id", { "id" :  flight_id}).rowcount == 0:
            return "Number flight not exist"
        else:
            db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
              {"name": name, "flight_id": flight_id})
            db.commit()
            return "Success"
    else:
        return "You shood enter name"
