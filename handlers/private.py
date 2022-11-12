from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# Murti Müzik tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@BOT_USERNAME"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/8351b6b8278d5e171f456.jpg",
                caption=(f"""● Merhaba {message.from_user.mention} \n\n● Ben Flas Muzik Bot !\n\n● Sesli Sohbetlerde Müzik Çalabilen Bir Botum . . ! \n\n● Ban Yetkisi Vermeden, Sesli Sohbet Yönetim Yetkisi Verip Asistanımı Gruba Ekleyin . . !"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Beni Gruba Ekle ➕", url=f"https://t.me/Sohbetala_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📗 Komutlar" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "✨ Grubumuz", url="https://t.me/kelebekailesi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌹 Kanalımız", url="https://t.me/musicflase"
                    )
                ]
                
           ]
        ),
    )



@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>📗 Komutlar : \n\n» /vbul => ᴠɪᴅᴇᴏ ɪɴᴅɪʀ \n» /cal => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ . \n» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ . \n» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ . \n» /atla =>  ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ . \n» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ . \n» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ . \n» /reload => ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜɴᴄᴇʟʟᴇʀ . \n\n» /auth => ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ʏᴏɴᴇᴛɪᴄɪ ᴏʟᴍᴀᴅɪɢɪ ʜᴀʟᴅᴇ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴋᴜʟʟᴀɴᴍᴀsɪɴᴀ ɪᴢɪɴ ᴠᴇʀɪʀ .  \n\n» /unauth => ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ʏᴏɴᴇᴛɪᴄɪ ᴏʟᴍᴀᴅɪɢɪ ʜᴀʟᴅᴇ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴋᴜʟʟᴀɴᴍᴀsɪɴɪ ᴇɴɢᴇʟʟᴇʀ . </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔱 Asistanım", url="https://t.me/asistanmucisflas"
                     ),
                     InlineKeyboardButton(
                         "👤 Sahip", url="https://t.me/Master_lockee"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "🔙 Geri 🔙", callback_data="cbstart")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""● Merhaba {query.from_user.mention} \n\n● Ben {bot} !\n\n●  Aradığınızı Bulamıyorsanız @Master_lockee İle İletişim'e Geçin . . ! \n\n● Keyifli Dinlemeler 🎵, Asistanım: @Master_lockee. . !""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Beni Gruba Ekle ➕", url=f"https://t.me/Sohbetala_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📗 Komutlar" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "🌹 Kanalımız", url=f"https://t.me/musicflase"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🖇️ Reklam", url="https://t.me/Master_lockee"
                    )
                ]
                
           ]
        ),
    )
