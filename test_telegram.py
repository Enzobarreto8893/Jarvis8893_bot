from config import * #importamos el token 
import telebot

#instaciamos el bot de telegram
bot = telebot.Telebot(Telegram_token) 	

#como responder al comando /start
@bot.message_handler(commands=["start", "ayuda", "help"])

def cmd_start(message):
"""da la bienvenida"""
bot.reply_to(message,"Hola!! mi nombre es Jarvis. En que te ayudo?" )

#Main

if _name_== '_main_':
   print ('iniciando Bot')
   bot.ininity_polling()	