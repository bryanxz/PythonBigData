from ftplib import print_line

import requests
import json
import pandas as pd

df=pd.read_csv('mercadolivreconsole - com plaintext.csv')

print(df.head(10))
# URL da API loca()l do Ollama
url = "http://localhost:11434/api/generate"

# Parâmetros para a geração de texto
print("Descrição: ")
descricao = input()
payloads = [

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", separada por vírgulas, analise se o console tem defeito. Se o console tiver qualquer defeito, responda apenas com o número 1. Se o console não tiver defeito ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", separada por vírgulas, analise se o console tem defeito na tela. Se o console tiver qualquer defeito na tela, responda apenas com o número 1. Se o console não tiver defeito na tela ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", separada por vírgulas, analise se o console tem defeito no hd. Se o console tiver qualquer defeito no hd, responda apenas com o número 1. Se o console não tiver defeito no hd ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", separada por vírgulas, analise se o console tem defeito na placa. Se o console tiver qualquer defeito na placa, responda apenas com o número 1. Se o console não tiver defeito na placa ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", separada por vírgulas, analise se o console tem defeito na fonte. Se o console tiver qualquer defeito na fonte, responda apenas com o número 1. Se o console não tiver defeito na fonte ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", separada por vírgulas, analise se o console tem defeito na carcaça. Se o console tiver qualquer defeito na carcaça, responda apenas com o número 1. Se o console não tiver defeito na carcaça ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", separada por vírgulas, analise se o console é modificado. Se o console for modificado, responda apenas com o número 1. Se o console não for modificado ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", separada por vírgulas, analise se o console é destravado. Se o console for destravado, responda apenas com o número 1. Se o console não for destravado ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", separada por vírgulas, analise se o console tem itens inclusos. Se o console tiver itens inclusos, responda apenas com o número 1. Se o console não tiver itens inclusos ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", separada por vírgulas, analise se o console tem jogos inclusos. Se o console tiver  jogos inclusos, responda apenas com o número 1. Se o console não tiver  jogos inclusos ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", responda a quantidade de jogos inclusos, se não tiver essa informação na descrição retorne 0. Não inclua mais nada na resposta, apenas o número de jogos inclusos."

    },

    {
        "model": "llama3.1:8b",  # Especifica o modelo 8B
        "prompt": "Com base na seguinte descrição: " + descricao + ", responda a quantidade de controles inclusos, se não tiver essa informação na descrição retorne 0. Não inclua mais nada na resposta, apenas o número de controles inclusos."

    },
]



# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json"
}

for payload in payloads:
# Faz a requisição POST para a API do Ollama
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    response_acumulator = ""
# Verifica se a requisição foi bem-sucedida
    for line in response.iter_lines():

        try:
                # Decodifica cada linha como JSON
            data = json.loads(line.decode('utf-8'))
          # Exibe o campo 'text'
            response_acumulator += data['response']
            print(data['response'])

        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            print(f"Linha com erro: {line}")


#print(response_acumulator)



