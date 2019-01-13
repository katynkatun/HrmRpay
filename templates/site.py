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