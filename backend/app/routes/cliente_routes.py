from flask import Blueprint, jsonify, request
from app import db
from app.models import Cliente

cliente_bp = Blueprint("cliente", __name__, url_prefix="/clientes")

@cliente_bp.route("", methods=["GET"])
def listar_clientes() :
    clientes = Cliente.query.all()
    return jsonify([c.to_dict() for c in clientes])


@cliente_bp.route("/<int:id>", methods=["GET"])
def obter_cliente(id) :
    cliente = Cliente.query.get_or_404(id)
    return jsonify(cliente.to_dict())


@cliente_bp.route("", methods=["POST"])
def criar_cliente() :
    dados = request.get_json()
    cliente = Cliente(
        nome=dados["nome"],
        email=dados["email"],
        telefone=dados["telefone"],
        endereco=dados.get("endereco")
    )

    db.session.add(cliente)
    db.session.commit()

    return jsonify(cliente.to_dict()), 201


@cliente_bp.route("/<int:id>", methods=["PUT"])
def atualizar_cliente(id) :
    cliente = Cliente.query.get_or_404(id)

    dados = request.get_json()

    cliente.nome = dados.get("nome", cliente.nome)
    cliente.email = dados.get("email", cliente.email)
    cliente.telefone = dados.get("telefone", cliente.telefone)
    cliente.endereco = dados.get("endereco", cliente.endereco)

    db.session.commit()

    return jsonify(cliente.to_dict())


@cliente_bp.route("/<int:id>", methods=["DELETE"])
def deletar_cliente(id) :
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()

    return "", 204