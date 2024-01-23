from config import * #importamos el token 
import telebot
import threading

#instaciamos el bot de telegram
bot = telebot.TeleBot(telegram_token) 	

#como responder al comando /start /ayuda /help
@bot.message_handler(commands=["start", "ayuda", "help"])

def cmd_start(message):
#da la bienvenida
   bot.reply_to(message,"Hola!! mi nombre es Lola. En que te ayudo?" )
   print(message.chat.id)
   
#como responder a los comandos de textos que no son comandos ya sea texto, audiio, video, etc
@bot.message_handler(content_types=["text"])
def bot_mensaje_texto(message):
   #recibe el mensaje y responde 
   if message.text.startswith("/"):
      foto=open(r"C:\Users\enzob\OneDrive\Escritorio\Jarvis8893_bot\Jarvis8893_bot\fotos_lola\enojada.jpg","rb")
      bot.send_photo(message.chat.id,foto, "Lola no sabe que quieres decir")
   else:
      foto=open(r"C:\Users\enzob\OneDrive\Escritorio\Jarvis8893_bot\Jarvis8893_bot\fotos_lola\bienvenida.jpg","rb")
      bot.send_photo(message.chat.id,foto, "Lola esta contenta de hablarte")

def recibir_mensajes():
   #comprueba si hay mensajes nuevos
   bot.infinity_polling()
#Main

if __name__== '__main__':
   print ('iniciando Bot')
   hilo_bot=threading.Thread(name="hilo_bot",target=recibir_mensajes)
   hilo_bot.start()
   print("Se inicio Bot")
   bot.send_message(MI_CHAT_ID,"Se inicio Bot")
   
     
     
      