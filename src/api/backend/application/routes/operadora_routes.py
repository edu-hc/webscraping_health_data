from flask import Blueprint, request, jsonify
from api.backend.application.services.operadora_service import OperadoraService
from config import Config

from api.backend.application.utils.sanitize_json import sanitize_json

# Criar Blueprint para rotas de operadoras
operadora_bp = Blueprint('operadora', __name__)

# Inicializar o serviço
operadora_service = OperadoraService()


@operadora_bp.route('/api/operadoras', methods=['GET'])
def buscar_operadoras():
    """
    Endpoint para buscar operadoras com base em um termo de busca
    """
    # Obter termo de busca da query string
    search_term = request.args.get('q', '')
    limit = int(request.args.get('limit', 25))  # Limite padrão: 25

    # Validar termo de busca
    if not search_term or len(search_term) < Config.MIN_SEARCH_LENGTH:
        return jsonify({
            'status': 'erro',
            'mensagem': f'É necessário fornecer um termo de busca com pelo menos {Config.MIN_SEARCH_LENGTH} caracteres',
            'results': []
        }), 400

    # Buscar operadoras
    try:
        resultados = operadora_service.search_operadoras(search_term, limit)

        # Sanitiza os dados para substituir valores inválidos
        sanitized_results = sanitize_json(resultados)

        return jsonify({
            'status': 'sucesso',
            'termo_busca': search_term,
            'total': len(sanitized_results),
            'results': sanitized_results
        })
    except Exception as e:
        return jsonify({
            'status': 'erro',
            'mensagem': f'Erro ao processar a busca: {str(e)}',
            'results': []
        }), 500


@operadora_bp.route('/api/operadoras/<registro_ans>', methods=['GET'])
def obter_operadora(registro_ans):
    """
    Endpoint para obter uma operadora específica pelo registro ANS
    """
    repository = operadora_service.repository
    operadora = repository.find_by_id(registro_ans)

    if operadora is None:
        return jsonify({
            'status': 'erro',
            'mensagem': f'Operadora com registro ANS {registro_ans} não encontrada'
        }), 404

    return jsonify({
        'status': 'sucesso',
        'operadora': operadora.to_dict()
    })