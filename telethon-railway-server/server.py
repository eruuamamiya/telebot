from fastapi import FastAPI
from telethon import TelegramClient
import os
from dotenv import load_dotenv

# Load variabel dari file .env
load_dotenv()

# Ambil API_ID dan API_HASH dari environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

# Inisialisasi FastAPI
app = FastAPI()

# Inisialisasi Telegram Client (Telethon)
client = TelegramClient('session', api_id, api_hash)

# Event untuk startup - mulai Telethon client
@app.on_event("startup")
async def startup_event():
    await client.start()

# Endpoint untuk ambil pesan dari channel
@app.get("/messages")
async def get_messages(channel: str):
    messages = []
    # Ambil pesan dari channel
    async for message in client.iter_messages(channel, limit=10):
        messages.append({
            "id": message.id,
            "text": message.text
        })
    return messages
