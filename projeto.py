#pip install flask

from flask import Flask, render_template, request

#criação de classe
class Aluno:
    def __init__(self, ra,  nome, idade, email):
        self.ra_aluno = ra
        self.nome_aluno = nome
        self.idade_aluno = idade
        self.email_aluno = email


#variavel inicial de aplicação
#contem as propriedades da minha aplicação
app = Flask(__name__)



#a linha abaixo cria uma rota
@app.route('/Hello')
def olá():
    return "<h2>Iniciando o projeto flask </h2>"

@app.route('/lista')
def lista_alunos():
    #as 3 linhas abaixo instancia alunos
    alunos1=Aluno('1001', 'Weslley', '20' , 'Weslley@gmail.com')
    alunos2=Aluno('1002', 'Fabio', '21' , 'fabio@gmail.com')
    alunos3=Aluno('1003', 'Patricia', '29' , 'patricia@gmail.com')

    lista_alunos_cadastrados = [alunos1,alunos2,alunos3]

    return render_template('lista.html', faculdade = 'FECAF', alunos = lista_alunos_cadastrados)

#nova rota
@app.route('/cadastrar')
def cadastrar_aluno():
    return render_template('cadastrar.html')

@app.route('/add_aluni')
def adicionar_aluno():

    #as variaveis abaixo vao receber os dados preenchidos
    ra_recebido = request.form['txtRa']
    nome_recibido = request.form['txtNome']
    idade_recebido = request.form['txtIdade']
    email_recebido = request.form['txtEmail']





# a linha abaixo tem que que ser a ultima linha do seu projeto
app.run(debug=True)
