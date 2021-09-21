from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://i.ibb.co/khRz42f/Turkish-Voice.jpg")
    await message.reply_text(
        f"""**Merhaba , Telegram için açık kaynaklı, Müzik botudur. 

Grubunuzun sesli Sohbet'inde müzik Çalabilirim. Ben Developer 🇹🇷 [𓄂Maho Ağa ࿐](https://t.me/Mahoaga)

Beni grubunuza ekleyin ve özgürce müzik çalın 😆!**
        """,
        reply_markup=InlineKeyboardMarkup(
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Müzik Aram Botu", url="https://github.com/Mp3_aramaBot")
                  ],[
                    InlineKeyboardButton(
                        "🚀 Etiket Tagger Botu", url="https://t.me/Mentiondavet_bot"
                    ),
                    InlineKeyboardButton(
                        "🏷️ Destek Kanalı", url="https://t.me/Sohbetdestek"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Grubunuza Ekle ➕", url="https://t.me/Efsanestar_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Bot Çalışıyor Sorun Yok**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛡 Kanal 🛡", url="https://t.me/Sohbetdestek")
                ]
            ]
        )
   )


