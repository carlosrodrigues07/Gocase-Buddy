# handler.py
import os
import json
import logging
from dotenv import load_dotenv
from services.telegram_service import (
    get_telegram_file,
    send_message,
    send_audio,
    download_file,
)
from services.bedrock_service import generate_humanized_response
from services.rekognition_service import detect_text, analyze_engagement
from services.lex_service import send_to_lex, handle_intent_response
from services.s3_service import upload_audio_to_s3

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Configurações do Amazon Lex
LEX_BOT_ID = os.getenv("LEX_BOT_ID")
LEX_ALIAS_ID = os.getenv("LEX_ALIAS_ID")
LEX_LOCALE_ID = os.getenv("LEX_LOCALE_ID")


def lambda_handler(event, context):
    """
    Ponto de entrada principal para processar eventos do bot do Telegram.
    """
    try:
        logger.info(f"Evento recebido: {json.dumps(event, indent=2)}")
        body = json.loads(event["body"])
        message = body.get("message", {})
        chat_id = str(message.get("chat", {}).get("id", ""))

        if not chat_id:
            return responder_erro("ID do chat não encontrado.")

        # Ignorar mensagens de bots
        if message.get("from", {}).get("is_bot"):
            return responder_sucesso()

        # Processar tipos de mensagens
        if "text" in message:
            processar_mensagem_texto(chat_id, message["text"])
        elif "photo" in message:
            processar_mensagem_imagem(chat_id, message["photo"][-1]["file_id"])

        return responder_sucesso()

    except Exception as e:
        logger.error(f"Erro no handler: {e}", exc_info=True)
        return responder_erro(str(e))


def processar_mensagem_texto(chat_id, texto):
    """
    Processa mensagens de texto interagindo com o Amazon Lex.
    """
    resposta_lex = send_to_lex(
        bot_id=LEX_BOT_ID,
        bot_alias_id=LEX_ALIAS_ID,
        locale_id=LEX_LOCALE_ID,
        session_id=chat_id,
        text=texto,
    )
    handle_intent_response(chat_id, resposta_lex)


def processar_mensagem_imagem(chat_id, file_id):
    """
    Processa mensagens com imagens, detectando texto e analisando engajamento.
    """
    caminho_arquivo = get_telegram_file(file_id)
    if not caminho_arquivo:
        return send_message(chat_id, "Falha ao processar a imagem.")

    imagem_bytes = download_file(caminho_arquivo)
    if not imagem_bytes:
        return send_message(chat_id, "Falha ao baixar a imagem.")

    # Detectar texto e engajamento na imagem
    texto_extraido = detect_text(imagem_bytes)
    engajamento = analyze_engagement(imagem_bytes)

    

def responder_sucesso():
    """
    Retorna uma resposta de sucesso.
    """
    return {"statusCode": 200}


def responder_erro(mensagem_erro):
    """
    Retorna uma resposta de erro.
    """
    return {"statusCode": 500, "body": json.dumps({"erro": mensagem_erro})}