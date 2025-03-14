# lex_service.py
import json
import logging
import boto3
from intents.saudacao import handle_saudacao_inicial
from intents.obter_briefing import handle_obter_briefing
from intents.tirar_duvidas import handle_tirar_duvidas
from intents.saber_endereco import handle_saber_endereco
from services.telegram_service import send_message


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

lex_client = boto3.client("lexv2-runtime", region_name="us-east-1")

def send_to_lex(bot_id, bot_alias_id, locale_id, session_id, text):
    """
    Envia uma mensagem para o Amazon Lex e retorna a resposta.
    """
    try:
        logger.info(f"Enviando para Lex: BotId={bot_id}, AliasId={bot_alias_id}, Texto={text}")
        response = lex_client.recognize_text(
            botId=bot_id,
            botAliasId=bot_alias_id,
            localeId=locale_id,
            sessionId=session_id,
            text=text
        )
        logger.debug(f"Resposta do Lex: {json.dumps(response, indent=2)}")
        return response
    except Exception as e:
        logger.error(f"Erro ao enviar mensagem para o Lex: {e}", exc_info=True)
        return None

def handle_intent_response(chat_id, lex_response):
    """
    Processa a resposta do Lex e envia a mensagem de texto diretamente para o Telegram.
    """
    logger.info(f"Resposta completa do Lex: {json.dumps(lex_response, indent=2)}")  # Adicione este log

    if lex_response and "interpretations" in lex_response:
        intent_name = lex_response["interpretations"][0]["intent"]["name"]
        logger.info(f"Intenção reconhecida: {intent_name}")

        if intent_name == "SaudacaoInicial":
            response_message = handle_saudacao_inicial()
        elif intent_name == "ObterBriefing":
            nome_influenciador = lex_response["interpretations"][0]["intent"].get("slots", {}).get("NomeInfluenciador", {}).get("value", {}).get("interpretedValue")
            response_message = handle_obter_briefing(nome_influenciador)
        elif intent_name == "TirarDuvidas":
            duvida = lex_response["interpretations"][0]["intent"].get("slots", {}).get("Duvida", {}).get("value", {}).get("interpretedValue")
            response_message = handle_tirar_duvidas(duvida)
        elif intent_name == "SaberEndereco":
            response_message = handle_saber_endereco()
        else:
            response_message = "Desculpe, não entendi sua solicitação."

        # Envia a mensagem de texto diretamente para o Telegram
        send_message(chat_id, response_message)
        return None  # Não precisa retornar nada, pois a mensagem já foi enviada

    logger.warning("Lex não retornou mensagens válidas. Gerando resposta padrão.")
    send_message(chat_id, "Não consegui processar sua mensagem.")
    return None