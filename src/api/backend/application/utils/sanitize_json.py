import math

def sanitize_json(data):
    """
    Substitui valores inválidos no JSON (NaN, Infinity, undefined) por null.
    """
    if isinstance(data, list):
        return [sanitize_json(item) for item in data]
    elif isinstance(data, dict):
        return {key: sanitize_json(value) for key, value in data.items()}
    elif isinstance(data, float) and (math.isnan(data) or math.isinf(data)):
        return None
    return data