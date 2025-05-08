from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Soy un bot sencillo desplegado en Koyeb 🎉.")

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Estos son los comandos disponibles:\n/start - Saludo inicial\n/help - Ayuda")

def main():
    # Token del Bot (obtenlo desde @BotFather en Telegram)
    BOT_TOKEN = "7725269349:AAFHd6AYWbFkUJ5OjSe2CjenMMjosD_JvD8"

    # Inicializar la aplicación del bot
    application = Application.builder().token(BOT_TOKEN).build()

    # Añadir manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Ejecutar el bot
    application.run_polling()

if __name__ == "__main__":
    main()
