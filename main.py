import requests
import json
import pandas as pd

# URL da API local do Ollama
url = "http://localhost:11434/api/generate"

# Ler o arquivo CSV
df = pd.read_csv('mercadolivreconsole.csv', encoding='ISO-8859-1')

print("Colunas disponíveis:", df.columns)

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json"
}

# Acumular resultados
resultados = []

# Definir as perguntas
perguntas = [
    ("defeito", "analise se o console tem defeito."),
    ("defeito na tela", "analise se o console tem defeito na tela."),
    ("defeito no hd", "analise se o console tem defeito no hd."),
    ("defeito na placa", "analise se o console tem defeito na placa."),
    ("defeito na fonte", "analise se o console tem defeito na fonte."),
    ("defeito na carcaça", "analise se o console tem defeito na carcaça."),
    ("modificado", "analise se o console é modificado."),
    ("destravado", "analise se o console é destravado."),
    ("itens inclusos", "analise se o console tem itens inclusos."),
    ("jogos inclusos", "analise se o console tem jogos inclusos."),
    ("quantidade de jogos", "responda a quantidade de jogos inclusos."),
    ("quantidade de controles", "responda a quantidade de controles inclusos."),
]

# Processar cada descrição do CSV
for descricao in df['descricao']:
    response_acumulator = ""

    for chave, pergunta in perguntas:
        payload = {
            "model": "llama3.1:8b",
            "prompt": f"Com base na seguinte descrição: {descricao}, separada por vírgulas, {pergunta} Se o console tiver qualquer defeito, responda apenas com o número 1. Se o console não tiver defeito ou se essa informação não estiver na descrição, responda apenas com o número 0. Não inclua mais nada na resposta, apenas o número."
        }

        # Faz a requisição POST para a API do Ollama
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            for line in response.iter_lines():
                try:
                    # Decodifica cada linha como JSON
                    data = json.loads(line.decode('utf-8'))
                    response_acumulator += data['response']
                    print(data['response'])  # Imprime a resposta
                except json.JSONDecodeError as e:
                    print(f"Erro ao decodificar JSON: {e}")
                    print(f"Linha com erro: {line}")
        else:
            print(f"Erro na requisição: {response.status_code}")

    # Armazena o resultado acumulado para cada descrição
    resultados.append(response_acumulator)

# Adiciona os resultados ao DataFrame
df['resultado'] = resultados

# Salva os resultados em um novo arquivo CSV
df.to_csv('resultado.csv', index=False)
