# bedrock_service.py
import boto3
import logging
import json

logger = logging.getLogger(__name__)
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def generate_humanized_response(prompt):
    """
    Gera uma resposta humanizada usando o Amazon Bedrock.
    """
    try:
        response = bedrock.invoke_model(
            modelId="anthropic.claude-v2",  # Modelo Claude da Anthropic
            body=json.dumps({
                "prompt": prompt,
                "max_tokens_to_sample": 300,
                "temperature": 0.7,
                "top_p": 0.9,
            }),
            contentType="application/json",
        )
        response_body = json.loads(response["body"].read())
        return response_body.get("completion", "Desculpe, não consegui gerar uma resposta.")
    except Exception as e:
        logger.error(f"Erro ao gerar resposta com Bedrock: {e}", exc_info=True)
        return "Desculpe, ocorreu um erro ao processar sua solicitação."