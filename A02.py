from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<H1>Bem-vindo à nossa cafeteria!</H1>"

@app.route("/menu")
def menu():
    return "Confira nosso menu..."

@app.route("/localizacao")
def localizacao():
    return render_template("localizacao.html")

app.run(debug=True)
