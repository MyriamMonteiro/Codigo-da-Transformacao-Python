from flask import Flask, request, jsonify
import sqlite3
from marshmallow import Schema, fields, ValidationError

class UsuarioSchema(Schema):
    nome = fields.Str(required=True)
    cidade = fields.Str(required=True)

usuario_schema = UsuarioSchema()

gerenciar_usuarios = Flask(__name__)

@gerenciar_usuarios.route('/apresentacao/<nome>', methods=['GET'])
def apresentacao(nome):
    return jsonify({"mensagem": f"Olá, {nome}! Bem-vindo(a) a uma API de Gerenciamento de Usuários."})


@gerenciar_usuarios.route('/cadastro', methods=['POST'])
def cadastro_usuario():
    informacoes = request.json
    nome = informacoes.get("nome")
    cidade = informacoes.get("cidade")


    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute("INSERT INTO usuarios (nome, cidade) VALUES (?, ?)", (nome, cidade))
    con.commit()
    con.close()

    return jsonify({"mensagem": "Cadastro concluído!.", "informacoes": informacoes})


def criar_tabela():
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT
        )
    """)
    con.commit()
    con.close()


@gerenciar_usuarios.route('/usuarios', methods=['GET'])
def listar_usuarios():
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM usuarios")
    usuarios = cur.fetchall()
    con.close()
    return jsonify(usuarios)


@gerenciar_usuarios.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    informacoes = request.json
    nome = informacoes.get("nome")
    cidade = informacoes.get("cidade")

    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute("UPDATE usuarios SET nome=?, cidade=? WHERE id=?", (nome, cidade, id))
    con.commit


@gerenciar_usuarios.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    con = sqlite3.connect("usuarios.db")
    cur = con.cursor()
    cur.execute("DELETE FROM usuarios WHERE id=?", (id,))
    con.commit()
    con.close()
    return jsonify({"mensagem": f" O usuário {id} foi deletado."})

