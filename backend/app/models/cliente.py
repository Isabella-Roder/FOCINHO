from app import db

class Cliente(db.Model) :
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(255))
    criado_em = db.Column(db.DateTime, server_default=db.func.now())

    pets = db.relationship("Pet", backref="tutor", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "endereco": self.endereco,
        }
