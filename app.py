from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html", titolo='Home Page')

@app.route("/details")
def details_page():
    return render_template("details.html", titolo="Details")

app.run()
