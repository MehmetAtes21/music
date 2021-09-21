from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("https://i.ibb.co/khRz42f/Turkish-Voice.jpg")
    await message.reply_text(
        f"""**Merhaba, {bn} 🎵

Sesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz. Düzen Tasarım [Talia Müzik 🎙️](https://t.me/Sohbetdestek).

Gruba ekle!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏷️ Destek Kanalı", url="https://t.me/Sohbetdestek")
                  ],[
                    InlineKeyboardButton(
                        "📣 Tagger Bot" , url = "https://t.me/Mentiondavet_bot"
                    ),
                    InlineKeyboardButton(
                        "🔊 Asistan" , url = "https://t.me/taliamusicasistant"""
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎶 Mp3 Botu", url="https://t.me/Mp3_aramaBot"
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
                        "🔊 Sahip", url="https://t.me/Mahoaga")
                ]
            ]
        )
   )


