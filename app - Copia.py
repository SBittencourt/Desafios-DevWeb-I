from flask import Flask, render_template
from flask_mysqldb import MySQL
app = Flask(__name__)

#Conexão com banco de dados
app.config['MYSQL_HOST'] = 'localhost' #127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config{'MYSQL_DB'] = 'fatec'

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/quemsomos')
def quemsomos():
   return render_template('quemsomos.html')

@app.route('/contato')
def contato():
           if request.method == "POST":
               email = request.form['email']
               assunto = request.form['assunto']
               descricao = request.form['descricao']
            
               cur = mysql.connection.cursor()
               cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES(%s,%s,%s)", (email, assunto, descricao))
               
               mysql.connection.commit()
               
               cur.close()
               return 'sucesso'
   return render_template('contato.html')
   
if __name__ == '__main__':
   app.run()
