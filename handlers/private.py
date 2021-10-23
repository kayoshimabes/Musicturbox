from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAADBQADKAIAAmQgIVd2e584kTrkUgI")
    await message.reply_text(
        f"""Hai 👋🏻, I am Music Telegram 🎵

I can play music in your group's voice call. Developed by [GLITTER](https://t.me/Biarenakliatnyaaa).

Add me to your group and play music freely!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎛 𝓒𝓸𝓶𝓶𝓪𝓷𝓭", url="https://telegra.ph/Musicturbox-Musik-04-24")
                  ],[
                    InlineKeyboardButton(
                        "💬 𝓖𝓻𝓸𝓾𝓹𝓼", url="https://t.me/Virtualllnihsad"
                    ),
                    InlineKeyboardButton(
                        "🔊 𝓒𝓱𝓪𝓷𝓷𝓮𝓵", url="https://t.me/whiteneey"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎁 𝓓𝓸𝓷𝓪𝓼𝓲", url="https://t.me/Biarenakliatnyaaa"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝓢𝓾𝓹𝓹𝓸𝓻𝓽 𝓒𝓱𝓪𝓷𝓷𝓮𝓵🌻", url="https://t.me/storeglitter")
                ]
            ]
        )
   )


