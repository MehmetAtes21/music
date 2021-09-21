from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("https://i.ibb.co/khRz42f/Turkish-Voice.jpg")
    await message.reply_text(
        f"""**Merhaba, {bn} 🎵
Sesli sohbette müzik botu. Ban yetkisiz ses yönetimi yetkisi verip asistanı gruba ekle  Geliştirici [🏷️ Talia Sohbet Destek](https://t.me/Sohbetdestek).
Gruba ekle!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🙋‍♂️ Beni Grubuna Ekle", url="https://t.me/Efsanestar_bot?startgroup=true"
                  ],[
                    InlineKeyboardButton(
                        "🎶 Mp3 botu" , url = "https://t.me/Mp3_aramaBot"
                    ),
                    InlineKeyboardButton(
                        "🎙️Asistanım " , url = "https://t.me/TaliaMusicAsistant"""
                    )
                ],[ 
                    InlineKeyboardButton(
                        "📣 Tagger Bot", url="https://t.me/Mentiondavet_bot"
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
                        "🏷️ Kanal", url="https://t.me/Sohbetdestekf")
                ]
            ]
        )
   )
