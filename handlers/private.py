from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**selam, {bn} 🎵

Sesli sohbette müzik botu. Ban yetkisiz ses yönetimi yetkisi verip asistanı gruba ekle  Geliştirici [BOSS](https://t.me/bosswolff).

Gruba ekle!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 DESTEK İLETİŞİM 🛠", url="https://t.me/bosswolff")
                  ],[
                    InlineKeyboardButton(
                        "💬 Komutlar" , url = "https://t.me/sohbetkuslari"
                    ),
                    InlineKeyboardButton(
                        "🔊 Asistan Gruba ekle yoksa çalışmaz" , url = "https://t.me/seslisohbetmuzik"""
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🇹🇷 Geliştirici 🇹🇷", url="https://t.me/bosswolff"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yeniden başlatıldı sorunsuz çalışıyor ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Sahip", url="https://t.me/bosswolff")
                ]
            ]
        )
   )


