from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página principal da livraria
@app.route('/')
def livraria():
    return render_template('livraria.html')

if __name__ == '__main__':
    app.run(debug=True)
