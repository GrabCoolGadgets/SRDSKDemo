from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start") & filters.private)
async def start_with_movie_name(client, message: Message):
    try:
        if len(message.command) > 1:
            movie_name = message.command[1]
            await message.reply_text(f"🔍 Searching for: **{movie_name}**")

            # Yaha aap apna search function laga sakte ho
            # For example:
            results = await custom_movie_search_function(movie_name)  # <-- Apna function call karo

            if results:
                await message.reply_text(f"✅ Results found for **{movie_name}**:\n\n{results}")
            else:
                await message.reply_text("❌ No results found.")
        else:
            await message.reply_text("👋 Welcome to the bot! Send a movie name after /start like:\n`/start Krrish3`")
    except Exception as e:
        await message.reply_text(f"⚠️ Error: {e}")

# 👇 Dummy search function (isse aap apne real search function se replace karo)
async def custom_movie_search_function(query):
    # yaha aap apne post search logic lagao ya telegraph post dhoondo
    if query.lower() == "krrish3":
        return "Krrish3 full HD [Download Now](https://t.me/yourchannel/1234)"
    else:
        return None
