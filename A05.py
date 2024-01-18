# main.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'
db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Float, nullable=False)

class ProdutoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    descricao = StringField('Descrição', validators=[DataRequired()])
    preco = StringField('Preço', validators=[DataRequired()])
    submit = SubmitField('Criar Produto')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ProdutoForm()

    if form.validate_on_submit():
        novo_produto = Produto(
            nome=form.nome.data,
            descricao=form.descricao.data,
            preco=form.preco.data
        )
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for('listar_produtos'))

    produtos = Produto.query.all()
    return render_template('index.html', form=form, produtos=produtos)

@app.route('/listar_produtos')
def listar_produtos():
    produtos = Produto.query.all()
    return render_template('listar_produtos.html', produtos=produtos)

@app.route('/editar/<int:produto_id>', methods=['GET', 'POST'])
def editar_produto(produto_id):
    produto = Produto.query.get(produto_id)
    form = ProdutoForm(obj=produto)

    if form.validate_on_submit():
        produto.nome = form.nome.data
        produto.descricao = form.descricao.data
        produto.preco = form.preco.data
        db.session.commit()
        return redirect(url_for('listar_produtos'))

    return render_template('editar_produto.html', form=form)

@app.route('/excluir/<int:produto_id>')
def excluir_produto(produto_id):
    produto = Produto.query.get(produto_id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('listar_produtos'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
