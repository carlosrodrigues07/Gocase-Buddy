import requests
import os
import logging

logger = logging.getLogger(__name__)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    logger.error("O token do Telegram (TELEGRAM_TOKEN) não está definido nas variáveis de ambiente.")

def get_telegram_file(file_id):
    """
    Obtém a URL de um arquivo enviado ao bot no Telegram.
    """
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getFile?file_id={file_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        file_path = response.json()["result"]["file_path"]
        logger.info(f"Arquivo do Telegram obtido: {file_path}")
        return f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}/{file_path}"
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao obter arquivo do Telegram: {e}")
        return None

def download_file(file_url):
    """
    Baixa um arquivo do Telegram usando sua URL.
    """
    try:
        response = requests.get(file_url, timeout=10)
        response.raise_for_status()
        logger.info(f"Arquivo baixado com sucesso: {file_url}")
        return response.content
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao baixar arquivo do Telegram: {e}")
        return None

def send_message(chat_id, text):
    """
    Envia uma mensagem de texto para o usuário no Telegram.
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Mensagem enviada com sucesso: {response.json()}")
    except requests.RequestException as e:
        logger.error(f"Erro ao enviar mensagem para o Telegram: {e}")

def send_audio(chat_id, audio_stream):
    """
    Envia um arquivo de áudio (MP3) para o usuário no Telegram.
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendAudio"
    files = {"audio": ("audio.mp3", audio_stream, "audio/mpeg")}
    payload = {"chat_id": chat_id}
    try:
        response = requests.post(url, data=payload, files=files, timeout=10)
        response.raise_for_status()
        logger.info(f"Áudio enviado com sucesso: {response.json()}")
    except requests.RequestException as e:
        logger.error(f"Erro ao enviar áudio para o Telegram: {e}")