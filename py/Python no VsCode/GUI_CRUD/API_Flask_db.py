import requests
from werkzeug.security import generate_password_hash
import sqlite3
from flask import Flask, jsonify, request
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ IMPLEMENTANDO FLASK'API'/TRATAMENTO DE EXCEÇOES/BANCO DE DADOS
def conection():
    connect_db = sqlite3.connect("banco.db")
    connect_db.row_factory = sqlite3.Row
    return connect_db

def run_db():
    connect_db = conection()
    connect_db.execute('''
        CREATE TABLE IF NOT EXISTS usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
        )
    ''')
    connect_db.commit()
    connect_db.close()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++FLASK
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"mensagem": "Bem Vindo!!"})


@app.route('/criar_usuario', methods=['POST'])
def create_users():
    data = request.get_json()    
    
    email = data['email']
    password = data['password']

    connect_db = conection()
    cursor = connect_db.cursor()

    hash_password = generate_password_hash(password)

    try:
        cursor.execute("INSERT INTO usuario (email,password) VALUES (?,?)", (email,hash_password))
        connect_db.commit()
      
        if data == None:
            return jsonify({"erro":"JSON ausente"}), 400
    
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({"erro":"Dados incompletos:\n Email e Password são obrigatórios"}),400
        
    except sqlite3.IntegrityError:
        return jsonify({"erro":"Email já cadastrado!"}),409
    except sqlite3.OperationalError:
        return jsonify({"erro":"Erro no servidor!"}),500
    except Exception:
        return jsonify({"erro":"Erro ao tentar processar!"}),500
    finally:
        connect_db.close()


    new_id = cursor.lastrowid

    return jsonify({
        "mensagem":"Usuario registrado com sucesso!",
        'id': new_id,
        'email': email
    }), 200

@app.route('/listar_usuarios', methods=['GET'])
def list_users():
    connect_db = conection()

    try:
        users = connect_db.execute("""SELECT id, email FROM usuario
                                    ORDER BY "id" ASC LIMIT 100
                                   """).fetchall()
    finally:
        connect_db.close()

    result = [{'id':user['id'],'email':user['email']} for user in users]
    return jsonify(result), 200

@app.route('/atualizar_usuario/<int:id>', methods=['PUT'])
def update_users(id):
    data = request.get_json()

    if not data or 'email' not in data:
        return jsonify({"erro": "O campo email deve ser obrigatório para atualizar!"}), 400

    new_email = data['email']

    try:
        connect_db = conection()
        cursor = connect_db.cursor()

        cursor.execute('UPDATE usuario SET email = ? WHERE id = ?', (new_email,id))
        connect_db.commit()
    
    finally:
        connect_db.close()

    return jsonify({"mesagem":f'Usuario {new_email} atualizado com sucesso!'}), 200

@app.route('/deletar_usuario/<int:id>', methods=['DELETE'])
def delete_users(id):
    connect_db = conection()
    cursor = connect_db.cursor()

    try:
        if id == None:
            return jsonify({"erro","ID não encontrado!"}), 404
        cursor.execute('DELETE FROM usuario WHERE id = ?', (id,))
        connect_db.commit()
    finally:
        connect_db.close()
    return jsonify({'mensagem':'Usuario deletado com sucesso!'}), 200

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ INICIALIZANDO O CRUD
if __name__ == "__main__":
    # Inicia o Banco de Dados
    run_db()
    # Inicia a API
    app.run(debug=True,port=5000)
