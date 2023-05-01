#!/usr/bin/env  python3


import requests
import os

os.system("cls")

# Insira o token do bot aqui
TOKEN = "5880526703:AAHZayZxHKtCx-4tQmoS3yPAg7t36zzvsCM"

# ID do chat para o qual deseja enviar a mensagem
chat_id = "-945678840"

# Texto da mensagem que deseja enviar
text = "Sosnielson, consegui te mandar mensagem"

# URL da API do Telegram para enviar a mensagem
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Parâmetros da mensagem (chat_id e texto)
params = {"chat_id": chat_id, "text": text}

# Enviar a mensagem usando a API do Telegram
response = requests.post(url, params=params)

# Verificar se a mensagem foi enviada com sucesso
if response.status_code == 200:
    print("Mensagem enviada com sucesso!")
else:
    print(f"Erro ao enviar mensagem: {response.text}")