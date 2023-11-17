from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    "host":"localhost",
    "user": "root",
    "password": "bil102030@",
    "database": "login"
}

@app.route("/")

def home():
    return "Bem vindo a minha API"


@app.route("/buscar_usuarios", methods=['GET'])
def buscar_usuarios():
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return jsonify({"usuarios": usuarios})

if __name__ == '__main__':
    app.run(debug=True)