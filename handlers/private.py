from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# Star MΓΌzik tarafΔ±ndan dΓΌzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/MTLXTSDCA4MLHScP7",
                caption=(f"""β **π¬πΎπππΊπ»πΊ** {message.from_user.mention} \n\nβ **π‘πΎπ** {bot} !\n\nβ **π²πΎπππ π²πππ»πΎπππΎππ½πΎ mΓΌzik π’πΊππΊπ»πππΎπ π‘ππππ . . !** \n\nβ **π‘πΊπ πΈπΎππππππ, π²πΎπ πΈπππΎπππ πΈπΎπππππ ππΎπππ π πππππΊππ π¦πππ»πΊ π€πππΎπππ . . !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π π‘πΎππ π¦πππ»πΊ π€πππΎ π", url=f"https://t.me/StarMuzikBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π πͺππππππΊπ" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "πΉπ· π’ππΊπππΎπ", url="https://t.me/StarBotKanal"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π§π»βπ» Ι’Ιͺα΄Κα΄Κ α΄α΄ΚΙ΄α΄α΄ α΄α΄α΄α΄ π§π»βπ»", url="https://github.com/MehmetAtes21/music"
                    )
                ]
                
           ]
        ),
    )



@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>πΉπ· TΓΌm Komutlar : \n\nΒ» /vbul => α΄ Ιͺα΄α΄α΄ ΙͺΙ΄α΄ΙͺΚ . \nΒ» /bul => α΄α΄α΄’Ιͺα΄ ΙͺΙ΄α΄ΙͺΚ . \nΒ» /oynat => α΄α΄α΄’Ιͺα΄ α΄ΚΙ΄α΄α΄ . \nΒ» /durdur => α΄α΄α΄’ΙͺΙ’Ιͺ α΄α΄Κα΄α΄Κ . \nΒ» /devam => α΄α΄α΄’ΙͺΙ’Ιͺ sα΄Κα΄α΄Κ . \nΒ» /atla =>  α΄α΄α΄’ΙͺΙ’Ιͺ α΄α΄Κα΄ . \nΒ» /son => α΄α΄α΄’ΙͺΙ’Ιͺ sα΄Ι΄Κα΄Ι΄α΄ΙͺΚ . \nΒ» /katil => α΄sΙͺsα΄α΄Ι΄Ιͺ Ι’Κα΄Κα΄ α΄α΄α΄ α΄α΄ α΄α΄α΄Κ . \nΒ» /reload => α΄α΄α΄ΙͺΙ΄ ΚΙͺsα΄α΄sΙͺΙ΄Ιͺ Ι’α΄Ι΄α΄α΄ΚΚα΄Κ . \n\nΒ» /auth => α΄α΄ΚΚα΄Ι΄Ιͺα΄ΙͺΙ΄ΙͺΙ΄ Κα΄Ι΄α΄α΄Ιͺα΄Ιͺ α΄Κα΄α΄α΄ΙͺΙ’Ιͺ Κα΄Κα΄α΄ α΄α΄α΄α΄α΄Κα΄ΚΙͺ α΄α΄ΚΚα΄Ι΄α΄α΄sΙͺΙ΄α΄ Ιͺα΄’ΙͺΙ΄ α΄ α΄ΚΙͺΚ .  \n\nΒ» /unauth => α΄α΄ΚΚα΄Ι΄Ιͺα΄ΙͺΙ΄ΙͺΙ΄ Κα΄Ι΄α΄α΄Ιͺα΄Ιͺ α΄Κα΄α΄α΄ΙͺΙ’Ιͺ Κα΄Κα΄α΄ α΄α΄α΄α΄α΄Κα΄ΚΙͺ α΄α΄ΚΚα΄Ι΄α΄α΄sΙͺΙ΄Ιͺ α΄Ι΄Ι’α΄ΚΚα΄Κ . </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "πΉπ· π πππππΊπ", url="https://t.me/StarMuzikAsistan"
                     ),
                     InlineKeyboardButton(
                         "π§π»βπ» π?πππΎπ", url="https://t.me/Hayiboo"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "β¬οΈ π¦πΎππ β¬οΈ", callback_data="cbstart")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""β **π¬πΎπππΊπ»πΊ** {query.from_user.mention} \n\nβ **π‘πΎπ** {bot} !\n\nβ **π²πΎπππ π²πππ»πΎπππΎππ½πΎ mΓΌzik π’πΊππΊπ»πππΎπ π‘ππππ . . !** \n\nβ **π‘πΊπ πΈπΎππππππ, π²πΎπ πΈπππΎπππ πΈπΎπππππ ππΎπππ π πππππΊππ π¦πππ»πΊ π€πππΎπππ . . !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π π‘πΎππ π¦πππ»πΊ π€πππΎ π", url=f"https://t.me/StarMuzikBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π πͺππππππΊπ" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "πΉπ· π’ππΊπππΎπ", url=f"https://t.me/StarBotKanal"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π§π»βπ» Ι’Ιͺα΄Κα΄Κ α΄α΄ΚΙ΄α΄α΄ α΄α΄α΄α΄ π§π»βπ»", url="https://github.com/MehmetAtes21/music"
                    )
                ]
                
           ]
        ),
    )
