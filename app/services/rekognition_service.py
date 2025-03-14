# rekognition_service.py
import boto3
import logging

logger = logging.getLogger(__name__)
rekognition = boto3.client("rekognition")

def detect_text(image_bytes):
    """
    Detecta texto em uma imagem usando o Amazon Rekognition.
    """
    try:
        response = rekognition.detect_text(Image={"Bytes": image_bytes})
        text_detections = response.get("TextDetections", [])
        logger.info(f"Texto detectado: {text_detections}")
        return " ".join(d["DetectedText"] for d in text_detections if d["Type"] == "LINE")
    except Exception as e:
        logger.error(f"Erro ao detectar texto: {e}", exc_info=True)
        return None

def detect_labels(image_bytes):
    """
    Detecta rótulos (labels) em uma imagem usando o Amazon Rekognition.
    """
    try:
        response = rekognition.detect_labels(Image={"Bytes": image_bytes}, MaxLabels=10)
        labels = [label["Name"] for label in response.get("Labels", [])]
        logger.info(f"Rótulos detectados: {labels}")
        return labels
    except Exception as e:
        logger.error(f"Erro ao detectar rótulos: {e}", exc_info=True)
        return None

def analyze_engagement(image_bytes):
    """
    Analisa o engajamento em uma postagem (ex: número de likes, comentários).
    """
    try:
        # Exemplo: Detectar rostos para estimar engajamento
        response = rekognition.detect_faces(Image={"Bytes": image_bytes}, Attributes=["ALL"])
        num_faces = len(response.get("FaceDetails", []))
        engagement_score = num_faces * 10  # Simulação de engajamento baseado em rostos
        logger.info(f"Engajamento estimado: {engagement_score}")
        return engagement_score
    except Exception as e:
        logger.error(f"Erro ao analisar engajamento: {e}", exc_info=True)
        return None