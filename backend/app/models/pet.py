from app import db

class Pet(db.Model) :
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    raca = db.Column(db.String(80))
    data_nascimento = db.Column(db.Date)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    criado_em = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self) :
        return {
            "id": self.id,
            "nome": self.nome,
            "especie": self.especie,
            "raca": self.raca,
            "data_nascimento": self.data_nascimento.isoformat() if self.data_nascimento else None,
            "cliente_id": self.cliente_id,
        }