# File: bot/plugins/website_start.py (FINAL GUARANTEED VERSION 4.0)

from pyrogram import Client, filters, enums
from pyrogram import StopPropagation
from pyrogram.types import Message  # <-- YEH LINE ADD KI GAYI HAI

# Hum aapke original search function ko uski sahi file se import kar rahe hain
from bot.plugins.group_filter import pm_filter 

# group=1 se iski priority sabse zyada ho jayegi
@Client.on_message(filters.command('start') & filters.private, group=1)
async def start_from_website(client: Client, message: Message):
    
    if len(message.command) > 1:
        
        payload = message.command[1]
        
        if payload.startswith("file_") or payload == "help":
            return

        movie_name_to_search = payload.replace("_", " ").strip()

#        await message.reply_text(
 #           f"⏳ Welcome! Searching for '<b>{movie_name_to_search}</b>' as requested from our website...",
 #           parse_mode=enums.ParseMode.HTML,
   #         disable_web_page_preview=True
 #       )
        
        message.text = movie_name_to_search
        await pm_filter(client, message)
        
        # Jab kaam ho jaaye, to process ko yahin rok do
        raise StopPropagation
