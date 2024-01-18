from flask import Flask
app = Flask(__name__)

# Rota para a página inicial da livraria
@app.route("/")
def homepage():
    return "Bem-vindo à Livraria Online!"

# Rota para a página de livros
@app.route("/livros")
def livros():
    return "Aqui estão os nossos livros..."

# Rota para a página de contato
@app.route("/contato")
def contato():
    return "Entre em contato conosco..."

app.run(debug=True)