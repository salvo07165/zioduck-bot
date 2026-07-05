import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
ENS_DOMAIN = "zioduck.eth"
products = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🦆 Bot di {ENS_DOMAIN} attivo.\n\n"
        "Comandi:\n/aggiungi Pizza 8€\n/lista\n/pubblica\n/svuota\n\n"
        f"Sito: https://{ENS_DOMAIN}.limo"
    )

async def aggiungi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Usa: /aggiungi Nome Prodotto 10€")
        return
    products.append(text)
    await update.message.reply_text(f"✅ Aggiunto: {text}\nTotale: {len(products)}")

async def lista(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not products:
        await update.message.reply_text("Lista vuota")
        return
    msg = "📦 Prodotti:\n\n" + "\n".join([f"{i+1}. {p}" for i, p in enumerate(products)])
    await update.message.reply_text(msg)

async def svuota(update: Update, context: ContextTypes.DEFAULT_TYPE):
    products.clear()
    await update.message.reply_text("🗑️ Svuotata")

async def pubblica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not products:
        await update.message.reply_text("Aggiungi prodotti prima")
        return
    await update.message.reply_text(f"✅ Fatto! Vai su https://{ENS_DOMAIN}.limo")

def main():
    print("Bot online")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aggiungi", aggiungi))
    app.add_handler(CommandHandler("lista", lista))
    app.add_handler(CommandHandler("pubblica", pubblica))
    app.add_handler(CommandHandler("svuota", svuota))
    app.run_polling()

if name == 'main':
    main()
