import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from web3 import Web3
from eth_account import Account

BOT_TOKEN = "8856869773:AAFx1-YjmgKSjk6lT3vukVnHvA_xAag_-PM"
PRIVATE_KEY = "0x4fc9f...89d25"  e4035f39b32f649b8404e0ef883185466456c6087717b7993fe3a894d3fbc0c6
ENS_DOMAIN = "zioduck.eth"
RPC_URL = "https://eth.llamarpc.com"

w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = Account.from_key(PRIVATE_KEY)
products = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🦆 Bot di {ENS_DOMAIN} attivo.\n\n"
        "Comandi:\n"
        "/aggiungi Pizza 8€\n"
        "/lista\n"
        "/pubblica\n"
        "/svuota\n\n"
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
    await update.message.reply_text(f"⏳ Pubblico {len(products)} prodotti...")
    html = f"<html><head><title>{ENS_DOMAIN}</title><meta charset='utf-8'>"
    html += "<style>body{font-family:sans-serif;max-width:600px;margin:40px auto;padding:20px}h1{color:#2563eb}li{padding:12px;border-bottom:1px solid #eee}</style></head>"
    html += f"<body><h1>🦆 {ENS_DOMAIN}</h1><h2>Prodotti</h2><ul>"
    for p in products: html += f"<li>{p}</li>"
    html += f"</ul><p>{len(products)} prodotti totali</p></body></html>"
    await update.message.reply_text(f"✅ Fatto! Vai su https://{ENS_DOMAIN}.limo\nAttendi 5 min la prima volta.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("aggiungi", aggiungi))
    app.add_handler(CommandHandler("lista", lista))
    app.add_handler(CommandHandler("pubblica", pubblica))
    app.add_handler(CommandHandler("svuota", svuota))
    print("Bot online")
    app.run_polling()

if name == 'main': main()
