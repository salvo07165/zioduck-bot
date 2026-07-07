from flask import Flask, send_file
from threading import Thread
import os
from telegram.ext import ApplicationBuilder, CommandHandler

# ---- PARTE WEB PER IL SITO ----
web = Flask('')

@web.route('/')
def home():
    return send_file('index.html')

def run_web():
    port = int(os.environ.get('PORT', 8080))
    web.run(host='0.0.0.0', port=port)

Thread(target=run_web).start()

# ---- PARTE BOT TELEGRAM ----
BOT_TOKEN = os.environ.get('BOT_TOKEN')  # Lo prendi da Variables su Railway

async def start(update, context):
    await update.message.reply_text("Ciao! Sono ZioDuck Bot")

def main():
    print("Bot online")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    # Aggiungi qui gli altri comandi: aggiungi, lista, svuota, pubblica
    app.run_polling()

if __name__ == "__main__":
    main()
