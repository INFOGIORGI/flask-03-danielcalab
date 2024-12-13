from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html", titolo='Home Page')

@app.route("/details")
def details_page():
    prodotti = (("pane", "s1", "1€"), ("carne", "s2", "10€"), ("pesce", "s3", "15€"))
    return render_template("details.html", titolo="Details", prodotti=prodotti)

app.run()
