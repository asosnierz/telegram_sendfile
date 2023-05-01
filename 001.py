import telegram
import asyncio

'''
métodos da classe Bot do Telegram:
    send_photo:Envia uma foto
    send_audio: Envia um arquivo de áudio.
    send_document: Envia um arquivo como documento.
    send_video: Envia um arquivo de vídeo.
    send_animation: Envia um arquivo de animação (GIF).
    send_voice: Envia um arquivo de voz.
    send_video_note: Envia uma nota de vídeo.
    send_sticker: Envia um sticker.
    send_contact: Envia um contato.
    send_location: Envia uma localização.
    send_venue: Envia uma localização com informações adicionais.
'''

TOKEN = '5880526703:AAHZayZxHKtCx-4tQmoS3yPAg7t36zzvsCM'
CHAT = '-945678840'
FILE = 'C:\\Users\\020163631\\Documents\\Pessoal\\Projetos\\telegram_sendfile\\001.txt'

async def send_file():
    with open(FILE, 'rb') as f:
        bot = telegram.Bot(token=TOKEN)
        await bot.send_document(chat_id=CHAT, document=f)
loop = asyncio.get_event_loop()
loop.run_until_complete(send_file())