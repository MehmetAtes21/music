from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/MTLXTSDCA4MLHScP7",
                caption=(f"""● **𝖬𝖾𝗋𝗁𝖺𝖻𝖺** {message.from_user.mention} \n\n● **𝖡𝖾𝗇** {bot} !\n\n● **𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝖽𝖾 müzik 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝖾𝗇 𝖡𝗈𝗍𝗎𝗆 . . !** \n\n● **𝖡𝖺𝗇 𝖸𝖾𝗍𝗄𝗂𝗌𝗂𝗓, 𝖲𝖾𝗌 𝖸𝗈𝗇𝖾𝗍𝗂𝗆 𝖸𝖾𝗍𝗄𝗂𝗌𝗂 𝗏𝖾𝗋𝗂𝗉 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾𝗒𝗂𝗇 . . !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 𝐁𝐞𝐧𝐢 𝐆𝐫𝐮𝐛𝐚 𝐄𝐤𝐥𝐞 🎉", url=f"https://t.me/SohbetMusicsBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🇹🇷 𝐀𝐬𝐢𝐬𝐭𝐚𝐧", url="https://t.me/SohbetMusicsAsistan"
                    ),
                    InlineKeyboardButton(
                        "📝 𝐒𝐚𝐡𝐢𝐩", url="https://t.me/ByWolk"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 𝐊𝐨𝐦𝐮𝐭𝐥𝐚𝐫" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📝 𝐊𝐚𝐧𝐚𝐥", url=f"https://t.me/StarBotKanal"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text("● **𝖭𝗈𝗍 :\n\n 𝖡𝗈𝗍𝗎𝗇 𝖠𝗄𝗍𝗂𝖿 𝖢𝖺𝗅𝗂𝗌𝗆𝖺𝗌𝗂 𝗂𝖼𝗂𝗇 𝖲𝗎 𝖴𝖼 𝗒𝖾𝗍𝗄𝗂𝗒𝖾 𝗂𝗁𝗍𝗂𝗒𝖺𝖼𝗂 𝖵𝖺𝗋𝖽𝗂𝗋 :\n\n> 𝖬𝖾𝗌𝖺𝗃𝗅𝖺𝗋𝗂 𝖲𝗂𝗅𝗆𝖾 ,\n> 𝖡𝖺𝗀𝗅𝖺𝗇𝗍𝗂 𝖣𝖺𝗏𝖾𝗍 𝖤𝗍𝗆𝖾 ,\n> 𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍 𝖸𝗈𝗇𝖾𝗍𝗆𝖾 ,**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "📚 𝖳𝗎𝗆 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", callback_data="herkes")
                 ],[
                     InlineKeyboardButton(
                         "🗯️ 𝖠𝗇𝖺 𝖬𝖾𝗇𝗎 ", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "📩 𝐒𝐚𝐡𝐢𝐩", url="https://t.me/ByWolk")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("● **𝖭𝗈𝗍 :\n\n 𝖡𝗈𝗍𝗎𝗇 𝖠𝗄𝗍𝗂𝖿 𝖢𝖺𝗅𝗂𝗌𝗆𝖺𝗌𝗂 𝗂𝖼𝗂𝗇 𝖲𝗎 𝖴𝖼 𝗒𝖾𝗍𝗄𝗂𝗒𝖾 𝗂𝗁𝗍𝗂𝗒𝖺𝖼𝗂 𝖵𝖺𝗋𝖽𝗂𝗋 :\n\n> 𝖬𝖾𝗌𝖺𝗃𝗅𝖺𝗋𝗂 𝖲𝗂𝗅𝗆𝖾 ,\n> 𝖡𝖺𝗀𝗅𝖺𝗇𝗍𝗂 𝖣𝖺𝗏𝖾𝗍 𝖤𝗍𝗆𝖾 ,\n> 𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍 𝖸𝗈𝗇𝖾𝗍𝗆𝖾 ,**", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "📚 𝖳𝗎𝗆 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "🗯️ 𝖠𝗇𝖺 𝖬𝖾𝗇𝗎", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "📩 𝐒𝐚𝐡𝐢𝐩", url="https://t.me/ByWolk")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>\n» /vbul => ᴠɪᴅᴇᴏ ɪɴᴅɪʀ . \n» /bul => ᴍᴜᴢɪᴋ ɪɴᴅɪʀ . \n» /oynat => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ . \n» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ . \n» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ . \n» /atla =>  ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ . \n» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ . \n» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ . \n» /reload => ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜɴᴄᴇʟʟᴇʀ .</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "📩 𝐒𝐚𝐡𝐢𝐩", url="https://t.me/ByWolk")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ 𝖦𝖾𝗋𝗂 ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler için komut menüsü 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/ByWolk")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""● **𝖬𝖾𝗋𝗁𝖺𝖻𝖺** {query.from_user.mention} \n\n● **𝖡𝖾𝗇** {bot} !\n\n● **𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝖽𝖾 müzik 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝖾𝗇 𝖡𝗈𝗍𝗎𝗆 . . !** \n\n● **𝖡𝖺𝗇 𝖸𝖾𝗍𝗄𝗂𝗌𝗂𝗓, 𝖲𝖾𝗌 𝖸𝗈𝗇𝖾𝗍𝗂𝗆 𝖸𝖾𝗍𝗄𝗂𝗌𝗂 𝗏𝖾𝗋𝗂𝗉 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾𝗒𝗂𝗇 . . !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 𝐁𝐞𝐧𝐢 𝐆𝐫𝐮𝐛𝐚 𝐄𝐤𝐥𝐞 🎉", url=f"https://t.me/SohbetMusicsBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🇹🇷 𝐀𝐬𝐢𝐬𝐭𝐚𝐧", url="https://t.me/SohbetMusicsAsistan"
                    ),
                    InlineKeyboardButton(
                        "📝 𝐒𝐚𝐡𝐢𝐩", url="https://t.me/ByWolk"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 𝐊𝐨𝐦𝐮𝐭𝐥𝐚𝐫" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📝 𝐊𝐚𝐧𝐚𝐥", url=f"https://t.me/StarBotKanal"
                    )
                ]
                
           ]
        ),
    )
