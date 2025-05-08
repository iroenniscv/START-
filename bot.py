import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, ContextTypes
)
from dotenv import load_dotenv
from website_monitor import (
    add_website, edit_website, check_status, scan_ports, ping_host, is_up
)
from utils import cancel_command

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_msg = (
        "¡Hola! Soy @watch_bot. Puedo vigilar tus sitios web y avisarte si fallan.\n\n"
        "📌 **Comandos disponibles:**\n"
        "/add - Agregar un sitio web\n"
        "/edit - Editar configuración\n"
        "/status - Estado de tus sitios\n"
        "/subscribe - Suscripción premium\n"
        "/metrics - Métricas de respuesta\n"
        "/ping - Hacer ping a un host\n"
        "/ports - Escanear puertos\n"
        "/isup - Verificar si un sitio está caído\n"
        "/cancel - Cancelar comando actual\n"
        "/help - Ayuda"
    )
    await update.message.reply_text(welcome_msg)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aquí tienes ayuda. 😊")

def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("add", add_website))
    app.add_handler(CommandHandler("edit", edit_website))
    app.add_handler(CommandHandler("status", check_status))
    app.add_handler(CommandHandler("ping", ping_host))
    app.add_handler(CommandHandler("ports", scan_ports))
    app.add_handler(CommandHandler("isup", is_up))
    app.add_handler(CommandHandler("cancel", cancel_command))

    app.run_polling()

if __name__ == "__main__":
    main()
