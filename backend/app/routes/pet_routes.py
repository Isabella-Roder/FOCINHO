from flask import Blueprint, jsonify, request
from app import db
from app.models import Pet

pet_bp = Blueprint("pet", __name__, url_prefix="/pets")

@pet_bp.route("", methods=["GET"])
def listar_pets() :
    pets = Pet.query.all()
    return jsonify([p.to_dict() for p in pets])


@pet_bp.route("/<int:id>", methods=["GET"])
def obter_pet(id) :
    pet = Pet.query.get_or_404(id)
    return jsonify(pet.to_dict())


@pet_bp.route("", methods=["POST"])
def criar_pet() :
    dados = request.get_json()

    pet = Pet (
        nome=dados["nome"],
        especie=dados["especie"],
        raca=dados.get("raca"),
        data_nascimento=dados.get("data_nascimento"),
        cliente_id=dados["cliente_id"]
    )

    db.session.add(pet)
    db.session.commit()

    return jsonify(pet.to_dict()), 201


@pet_bp.route("/<int:id>", methods=["PUT"])
def atualizar_pet(id) :
    pet = Pet.query.get_or_404(id)
    dados = request.get_json()

    pet.nome = dados.get("nome", pet.nome)
    pet.especie = dados.get("especie", pet.especie)
    pet.raca = dados.get("raca", pet.raca)
    pet.data_nascimento = dados.get("data_nascimento", pet.data_nascimento)

    db.session.commit()

    return jsonify(pet.to_dict())


@pet_bp.route("/<int:id>", methods=["DELETE"])
def deletar_pet(id) :
    pet = Pet.query.get_or_404(id)
    db.session.delete(pet)
    db.session.commit()
    return "", 204