import os
from flask import Flask, jsonify
from flask_cors import CORS

from api.backend.application.routes.operadora_routes import operadora_bp
from config import Config


def create_app():
    """
    Cria e configura a aplicação Flask
    """
    app = Flask(__name__)
    CORS(app)

    # Registrar blueprints
    app.register_blueprint(operadora_bp)

    # Rota inicial
    @app.route('/', methods=['GET'])
    def home():
        """Página inicial da API"""
        return jsonify({
            'status': 'online',
            'mensagem': 'API de busca de operadoras de saúde',
            'endpoints': {
                '/api/operadoras': 'GET - Buscar operadoras (parâmetro q=termo_busca)',
                '/api/operadoras/<registro_ans>': 'GET - Obter operadora específica'
            }
        })

    return app