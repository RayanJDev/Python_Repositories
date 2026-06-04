import tkinter as tk
from tkinter import messagebox, ttk
from werkzeug.security import generate_password_hash
import sqlite3
from flask import Flask, jsonify, request
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"mensagem": "Ola pessoal"})

@app.route('/criar_usuario', methods=['POST'])
def create_users():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"erro":"Dados incompletos:\n Email e Password são obrigatórios"})
    email = data['email']
    password = data['password']

    connect_db = conection()
    cursor = connect_db.cursor()

    hash_password = generate_password_hash(password)

    cursor.execute("INSERT INTO usuario (email,password) VALUES (?,?)", (email,hash_password))
    connect_db.commit()

    new_id = cursor.lastrowid
    connect_db.close()

    return jsonify({
        "mensagem":"Usuario registrado com sucesso!",
        'id': new_id,
        'email': email
    }), 201

@app.route('/listar_usuarios', methods=['GET'])
def list_users():
    connect_db = conection()

    users = connect_db.execute("SELECT id, email FROM usuario").fetchall()
    connect_db.close()

    result = [{'id':user['id'],'email':user['email']} for user in users]
    return jsonify(result), 200

@app.route('/atualizar_usuario/<int:id>', methods=['PUT'])
def update_users(id):
    data = request.get_json()

    if not data or 'email' not in data:
        return jsonify({"erro": "O campo email deve ser obrigatório para atualizar!"}), 400

    new_email = data['email']

    connect_db = conection()
    cursor = connect_db.cursor()

    cursor.execute('UPDATE usuario SET email = ? WHERE id = ?', (new_email,id))
    connect_db.commit()
    connect_db.close()

    return jsonify({"mesagem":f'Usuario {new_email} atualizado com sucesso!'}), 200

@app.route('/deletar_usuario/<int:id>', methods=['DELETE'])
def delete_users(id):
    connect_db = conection()
    cursor = connect_db.cursor()

    cursor.execute('DELETE FROM usuario WHERE id = ?', (id,))
    connect_db.commit()
    connect_db.close()

    return jsonify({'mensagem':'Usuario deletado com sucesso!'}), 200

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == "__main__":
    run_db()
    app.run(debug=True,port=5000)

