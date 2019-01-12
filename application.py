from flask import Flask, render_template, request, session
from flask_session import Session

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