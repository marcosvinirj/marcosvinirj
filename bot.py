import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from Educador_financeiro import main

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update, context):
    user_name = update.message.from_user.first_name
    #pegar salario
    #pegar renda extra
    #etc.

    dados = main(user_name, "22", "2000", "1000", "2000", "100")
    await update.message.reply_text(f'Olá, {user_name}! Bem-vindo ao seu bot do Telegram.')
    await update.message.reply_text(str(dados))

# Função para lidar com mensagens de texto
def echo(update, context):
    user_name = update.message.from_user.first_name
    message_text = update.message.text
    update.message.reply_text(f'{user_name}, você disse: {message_text}')

if __name__ == '__main__':
    application = ApplicationBuilder().token('6972850754:AAEdNoDj0wEdJdKZb62tgT2UbOFfQ0n72_A').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()