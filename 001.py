import telegram.ext
import asyncio

from telegram.ext import Updater, CommandHandler
from telegram import InputFile, InputMediaDocument

async def send_file():
    # meu token do seu bot
    bot = telegram.Bot(token='35880526703:AAHZayZxHKtCx-4tQmoS3yPAg7t36zzvsCM')

    # caminho e nome do seu arquivo
    with open('C:/Users/LAB/Documents/Python/001.txt', 'rb') as f:
        file = InputFile(f)

    # ID do chat que você deseja enviar o arquivo
    chat_id = '-945678840'

    # Cria um novo documento de mídia
    document = InputMediaDocument(file)

    # Envia o arquivo e espera a conclusão da operação
    await bot.send_media_group(chat_id=chat_id, media=[document])

# Executa a função assíncrona dentro de um loop de eventos
asyncio.run(send_file())
