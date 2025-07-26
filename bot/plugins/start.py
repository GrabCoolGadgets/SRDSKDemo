from pyrogram import Client, filters

@Client.on_message(filters.command("test"))
async def test_cmd(client, message):
    await message.reply("Bot is working fine ✅")
