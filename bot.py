import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
ENS_DOMAIN = "zioduck.eth"
products = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🦆 Bot di {ENS_DOMAIN} attivo.\n\n"
        "Comandi:\n/aggiungi Pizza 8€\n/lista\n/pubblica\n/svuota\n"
        f"Sito: https://{ENS_DOMAIN}.limo"
    )

async def aggiungi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Usa: /aggiungi Nome Prodotto")
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
    await update.message.reply_text(f"📢 Pubblicato su {ENS_DOMAIN}.limo")

def main():
    print("Bot online")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aggiungi", aggiungi))
    app.add_handler(CommandHandler("lista", lista))
    app.add_handler(CommandHandler("svuota", svuota))
    app.add_handler(CommandHandler("pubblica", pubblica))
    app.run_polling()

if name == "main":
    main()
