def analizar_texto_oferta(texto: str) -> dict:
    """
    Esta función después llamará al modelo de IA.
    Por ahora devuelve datos mock.
    """

    return {
        "titulo": "Backend Developer",
        "empresa": "Empresa Demo",
        "ubicacion": "Montevideo / Remote",
        "descripcion": texto,
        "cualidades": "Python, FastAPI",
        "seniority": "Junior",
        "salario": None
    }