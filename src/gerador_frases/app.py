from flask import Flask, render_template, request, redirect, url_for, session
from src.gerador_frases.utils.gerador import gerar_frase, coluna1, coluna2, coluna3, coluna4

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

@app.route('/')
def index():
    if 'historico' not in session:
        session['historico'] = []
    return render_template('index.html', historico=session['historico'])

@app.route('/gerar_frase')
def gerar():
    frase = gerar_frase()
    session['historico'].append(frase)
    session.modified = True
    return render_template('index.html', frase=frase, historico=session['historico'])

@app.route('/editar_colunas')
def editar_colunas():
    return render_template('editar_colunas.html', coluna1=coluna1, coluna2=coluna2, coluna3=coluna3, coluna4=coluna4)


@app.route('/adicionar_item/<int:coluna>', methods=['GET', 'POST'])
def adicionar_item(coluna):
    if request.method == 'POST':
        novo_item = request.form['texto']
        if coluna == 1:
            coluna1.append(novo_item)
        elif coluna == 2:
            coluna2.append(novo_item)
        elif coluna == 3:
            coluna3.append(novo_item)
        elif coluna == 4:
            coluna4.append(novo_item)
        return redirect(url_for('editar_colunas'))
    return render_template('adicionar_item.html', coluna=coluna)

if __name__ == '__main__':
    app.run(debug=True)