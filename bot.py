import telebot
from Educador_financeiro import main
# import decouple
# from Educador_financeiro import main as calculo

bot = telebot.TeleBot(
    "6972850754:AAEdNoDj0wEdJdKZb62tgT2UbOFfQ0n72_A", parse_mode=None)


def verificar_mensagem(mensagem):
    return True

@bot.message_handler(func=lambda message: True)
def welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message, f'Bem vindo {name} ao bot de educador financeiro!\nQual a sua idade?')

@bot.message_handler(func=welcome)
def get_age(message):
    idade = message.text
    bot.reply_to(message, 'Qual o seu salário?')
    bot.register_next_step_handler(message, get_salary, idade)

def get_salary(message, idade):
    salario = message.text
    bot.reply_to(message, 'Qual a sua renda extra?')
    bot.register_next_step_handler(message, get_extra_income, idade, salario)

def get_extra_income(message, idade, salario):
    renda_extra = message.text
    bot.reply_to(message, 'Qual o seu limite de gastos?')
    bot.register_next_step_handler(message, get_spending_limit, idade, salario, renda_extra)

def get_spending_limit(message, idade, salario, renda_extra):
    limite_gasto = message.text
    bot.reply_to(message, 'Qual a sua dívida extra?')
    bot.register_next_step_handler(message, calculate, idade, salario, renda_extra, limite_gasto)

def calculate(message, idade, salario, renda_extra, limite_gasto):
    divida_extra = message.text
    calculo = main(idade, salario, renda_extra, limite_gasto, divida_extra)

    bot.send_message(message.chat.id, f'Ok, seu nome é {calculo["nome"]}.')
    bot.send_message(message.chat.id, f'Ok, sua idade é {idade}.')
    bot.send_message(message.chat.id, f'Ok, seu salário é {salario}.')
    bot.send_message(message.chat.id, f'Ok, sua renda extra é {renda_extra}.')
    bot.send_message(message.chat.id, f'Ok, seu limite de gastos é {limite_gasto}.')
    bot.send_message(message.chat.id, f'Ok, sua dívida extra é {divida_extra}.')

bot.polling()