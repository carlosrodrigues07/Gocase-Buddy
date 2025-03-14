# s3_service.py
import boto3
import logging
import uuid
import os

logger = logging.getLogger(__name__)
s3 = boto3.client("s3")
BUCKET_NAME = os.environ.get("BUCKET_NAME")

def upload_audio_to_s3(audio_stream, chat_id):
    file_name = f"audio_{chat_id}_{uuid.uuid4().hex}.mp3"
    try:
        logger.info(f"Fazendo upload do áudio para S3: {file_name}")
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=audio_stream,
            ContentType="audio/mpeg"
        )
        audio_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{file_name}"
        logger.info(f"Áudio enviado com sucesso! URL: {audio_url}")
        return audio_url
    except Exception as e:
        logger.error(f"Erro ao fazer upload do áudio para o S3: {str(e)}")
        raise e