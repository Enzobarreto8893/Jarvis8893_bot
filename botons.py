from config import *
import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply

    
#insatanciamos el bot de telegram
bot= telebot.TeleBot(telegram_token)
usuarios ={}



#Luego, puedes utilizar este teclado en tu mensaje
@bot.message_handler(commands=['iniciar'])
def cmd_start(message):
   bot.send_message(message.chat.id, "Usa el comando /alta para comenzar a usar el bot")

@bot.message_handler(commands=['alta'])
def cmd_alta(message):
    #comienza a tomar los datos del usuario
    markup=ForceReply()
    mensaje=bot.send_message(message.chat.id, "Hola! soy Lola ¿como es tu nombre?", reply_markup=markup)
    bot.register_next_step_handler(mensaje, pregunta_edad)

def pregunta_edad(message):
    #pregunta la edad
    usuarios[message.chat.id]={}
    usuarios[message.chat.id]["nombre"] = message.text
    markup=ForceReply()
    mensaje=bot.send_message(message.chat.id, "¿cuantos años tienes?", reply_markup=markup)
    bot.register_next_step_handler(mensaje, preguntar_sexo)
    
def preguntar_sexo(message):
    # si la edad no es la correcta, vuelve a preguntar
    if not message.text.isdigit():
        markup = ForceReply()
        mensaje = bot.send_message(message.chat.id, "Por favor, ingresa un número.\n ¿cuántos años tienes?")
        # ejecutamos de nuevo la función
        bot.register_next_step_handler(mensaje, preguntar_sexo)
    else:
        usuarios[message.chat.id]["edad"] = int(message.text)
        # si la edad es correcta
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder='Pulsa un botón')
        markup.add("Hombre", "Mujer")
        # preguntamos el sexo
        mensaje = bot.send_message(message.chat.id, "¿cuál es tu sexo?", reply_markup=markup)
        bot.register_next_step_handler(mensaje, guardar_datos_usuarios)

# Corrección de la indentación de la función guardar_datos_usuarios
def guardar_datos_usuarios(message):
    # guardamos los datos del usuario
    if message.text != "Hombre" and message.text != "Mujer":
        # informamos que el dato ingresado es un error
        mensaje = bot.send_message(message.chat.id, "Sexo no válido. Por favor, pulsa un botón")
        bot.register_next_step_handler(mensaje, guardar_datos_usuarios)
    else:
        # el sexo es correcto
        usuarios[message.chat.id]["sexo"] = message.text
        texto = "Gracias por registrarte!\n"
        texto += f'<code>NOMBRE:</code> {usuarios[message.chat.id]["nombre"]}\n'
        texto += f'<code>EDAD..:</code> {usuarios[message.chat.id]["edad"]}\n'
        texto += f'<code>SEXO..:</code> {usuarios[message.chat.id]["sexo"]}\n'
        bot.send_message(message.chat.id, texto, parse_mode="html")
        print(usuarios)

# MAIN 
if __name__ == '__main__':
    print ('iniciando Bot')
    bot.infinity_polling()
    