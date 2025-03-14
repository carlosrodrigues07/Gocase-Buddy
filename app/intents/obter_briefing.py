# obter_briefing.py
def handle_obter_briefing(nome_influenciador=None):
    """
    Lida com a solicitação de briefing da campanha.
    Se o nome do influenciador não for fornecido, solicita o nome.
    """
    if not nome_influenciador:
        return "Antes de enviar o briefing, qual é o seu nome?"
    else:
        briefing = (
            "**Título da Campanha**: Estilo Personalizado com Gocase\n"
            "**Descrição**:\n"
            "A Gocase está lançando uma nova linha de acessórios personalizados, incluindo capinhas para celular, "
            "garrafas térmicas e mochilas. Queremos que você mostre como esses produtos combinam com seu estilo único!\n\n"
            "**Produtos Enviados**:\n"
            "- 1 capinha personalizada\n"
            "- 1 garrafa térmica\n"
            "- 1 mochila\n\n"
            "**Prazos**:\n"
            "- Data de postagem: [Data a ser definida]\n"
            "- Marcar @gocaseoficial e usar as hashtags #Gocase #EstiloPersonalizado\n\n"
            "**Expectativas**:\n"
            "- 1 postagem no feed do Instagram\n"
            "- 1 story destacando os produtos\n\n"
            "**Dúvidas?**:\n"
            "Entre em contato conosco ou responda a esta mensagem!"
        )
        return f"Aqui está o briefing da campanha, {nome_influenciador}:\n\n{briefing}"