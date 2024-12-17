from flask import Flask, render_template

app = Flask(__name__)
prodotti = (("pane", "s1", "1€"), ("carne", "s2", "10€"), ("pesce", "s3", "15€"), ("Fette Biscottate", "s1", "1,50€"))

@app.route("/")
def home_page():
    return render_template("home.html", titolo='Home Page')

@app.route("/details")
def details_page():
    return render_template("details.html", titolo="Details", prodotti=prodotti)

@app.route("/dettagli/<idS>")
def dettagliscaffale(idS):

    listaP = []
    for prodotto in prodotti:
        if prodotto[1]==idS:
            listaP.append(prodotto)
            
    print(listaP)
    return render_template("dettagliscaffale.html", titolo="Dettagli scaffale",listaP=listaP, numScaffale=idS)

app.run(debug=True)
