import os
import json
import boto3

from aws_lambda_powertools import Logger, Tracer

# Correcao de enunciado: o bloco "VOCE COMPLETA AQUI" no handler() e
# intencionalmente enxuto — ele NAO traz a solucao pronta nem um esqueleto quase
# copiavel; ler o S3 e tratar o erro e com voce. Este e o estado correto do
# arquivo, nao uma versao incompleta: nao ha nada a "restaurar" de um commit
# anterior.

logger = Logger(service="pedeja-api")
tracer = Tracer(service="pedeja-api")

s3 = boto3.client("s3")
BUCKET = os.environ["BUCKET_DATA_LAKE"]
CHAVE_RESUMO = "resumo/faturamento.json"


def resposta(status, corpo):
    """Monta a resposta HTTP no formato que o API Gateway espera. Ja pronto."""
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(corpo, ensure_ascii=False),
    }


@logger.inject_lambda_context
@tracer.capture_lambda_handler
def handler(event, context):
    # A API Gateway (proxy) invoca esta Lambda com um EVENTO — nao ha porta
    # escutando. Aqui respondemos GET /faturamento lendo o resumo do S3.

    # -- VOCE COMPLETA AQUI (bloco 3: servir) -----------------------------
    # Leia o resumo gravado pelo bloco 2 (objeto CHAVE_RESUMO no bucket BUCKET)
    # e transforme-o no dict `faturamento` devolvido abaixo. Pense no caminho
    # infeliz: se o bloco 2 ainda nao rodou, o objeto nao existe — trate esse
    # caso devolvendo `resposta(404, ...)` com uma mensagem clara, para a API
    # nao estourar um 500 generico.
    faturamento = {}
    # ---------------------------------------------------------------------

    logger.info("faturamento servido", cidades=len(faturamento))
    return resposta(200, faturamento)
