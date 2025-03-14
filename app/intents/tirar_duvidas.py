# tirar_duvidas.py
def handle_tirar_duvidas(duvida=None):
    """
    Lida com a solicitação de tirar dúvidas.
    Se a dúvida não for fornecida, solicita a dúvida.
    """
    if not duvida:
        return "Claro! Qual é a sua dúvida?"
    else:
        return "Anotamos sua dúvida e entraremos em contato em breve com a resposta. Obrigado!"