""" global banned and un-global banned module """

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from helpers.filters import command
from helpers.decorators import sudo_users_only
from helpers.dbchat import get_served_chats
from helpers.dbpunish import add_gban_user, is_gbanned_user, remove_gban_user

from config import BOT_NAME, SUDO_USERS, BOT_USERNAME as bn


@Client.on_message(command(["gban", f"gban@{bn}"]) & ~filters.edited)
@sudo_users_only
async def global_banned(c: Client, message: Message):
    if not message.reply_to_message:
        if len(message.command) < 2:
            await message.reply_text("**kullanım:**\n\n/gban [Kullanıcı adı | kullanıcı id]")
            return
        user = message.text.split(None, 2)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await c.get_users(user)
        from_user = message.from_user
        BOT_ID = await c.get_me()
        if user.id == from_user.id:
            return await message.reply_text(
                "You can't gban yourself !"
            )
        elif user.id == BOT_ID:
            await message.reply_text("Kendimi gban yapamam !")
        elif user.id in SUDO_USERS:
            await message.reply_text("sudo kullanıcısını gban yapamazsınız !")
        else:
            await add_gban_user(user.id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"🚷 **küresel yasaklama {user.mention}**\n⏱ Beklenen zaman: `{len(served_chats)}`"
            )
            number_of_chats = 0
            for num in served_chats:
                try:
                    await c.ban_chat_member(num, user.id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
🚷 **Yeni Küresel yasak [{BOT_NAME}](https://t.me/{bn})
**origin:** {message.chat.title} [`{message.chat.id}`]
**Sudo kullanıcı:** {from_user.mention}
**Banned kullanıcı:** {user.mention}
**Banned kullanıcı ID:** `{user.id}`
**sohbetler:** `{number_of_chats}`"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
        return
    from_user_id = message.from_user.id
    from_user_mention = message.from_user.mention
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    BOT_ID = await c.get_me()
    if user_id == from_user_id:
        await message.reply_text("kendi kendine gban yapamazsın !")
    elif user_id == BOT_ID:
        await message.reply_text("kendimi gban yapamam !")
    elif user_id in SUDO_USERS:
        await message.reply_text("sudo kullanıcısını gban yapamazsınız !")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if is_gbanned:
            await message.reply_text("Bu kullanıcı zaten gbanlı !")
        else:
            await add_gban_user(user_id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"🚷 **küresel yasaklama {mention}**\n⏱ Beklenen zaman: `{len(served_chats)}`"
            )
            number_of_chats = 0
            for num in served_chats:
                try:
                    await c.ban_chat_member(num, user_id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
🚷 **Yeni Küresel yasak [{BOT_NAME}](https://t.me/{bn})
**Origin:** {message.chat.title} [`{message.chat.id}`]
**Sudo kullanıcı:** {from_user_mention}
**Banned kullanıcı:** {mention}
**Banned kullanıcı ID:** `{user_id}`
**sohbetler:** `{number_of_chats}`"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
            return


@Client.on_message(command(["ungban", f"ungban@{bn}"]) & ~filters.edited)
@sudo_users_only
async def ungban_global(c: Client, message: Message):
    chat_id = message.chat.id
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**kullanım:**\n\n/ungban [Kullanıcı adı | kullanıcı id]"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await c.get_users(user)
        from_user = message.from_user
        BOT_ID = await c.get_me()
        if user.id == from_user.id:
            await message.reply_text("Kendinizi banlayamazsınız çünkü gbanlanamazsınız !")
        elif user.id == BOT_ID:
            await message.reply_text("Kendimi banlayamam çünkü gbann olamam !")
        elif user.id in SUDO_USERS:
            await message.reply_text("Sudo kullanıcıları gbanlı/gbansiz olamaz !")
        else:
            is_gbanned = await is_gbanned_user(user.id)
            if not is_gbanned:
                await message.reply_text("Bu kullanıcının yasağı kaldırılmadı !")
            else:
                await c.unban_chat_member(chat_id, user.id)
                await remove_gban_user(user.id)
                await message.reply_text("✅ Bu kullanıcının yasağı kaldırıldı")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    BOT_ID = await c.get_me()
    if user_id == from_user_id:
        await message.reply_text("Kendinizi banlayamazsınız çünkü gbanlanamazsınız !")
    elif user_id == BOT_ID:
        await message.reply_text(
            "Kendimi banlayamam çünkü gbann olamam !"
        )
    elif user_id in SUDO_USERS:
        await message.reply_text("Sudo kullanıcıları olamaz gbanned/ungbanned !")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if not is_gbanned:
            await message.reply_text("Bu kullanıcı gbanlı değil !")
        else:
            await c.unban_chat_member(chat_id, user_id)
            await remove_gban_user(user_id)
            await message.reply_text("✅ Bu kullanıcının yasağı kaldırıldı")
