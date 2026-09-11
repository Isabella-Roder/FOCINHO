from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app() :
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from app.models import Cliente, Pet

    @app.route("/")
    def index() :
        return jsonify({"status": "ok", "message": "Focinho API rodando"})

    return app