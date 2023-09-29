from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from config import API_HASH, API_ID, SESSION_NAME
from pyrogram import Client

from . import queues

client = Client(SESSION_NAME, API_ID, API_HASH)
pytgcalls = PyTgCalls(client)

@pytgcalls.on_stream_end()
async def on_stream_end(context, is_connected):
    chat_id = -1001983841726 - context.full_chat.id
    if is_connected:
        await app.send_message(chat_id, 'Successfully joined!')
    else:
        await app.send_message(chat_id, 'Disconnected from voice chat..')


@Client.on_message(filters.outgoing & filters.command('join'))
async def join_handler(_, message):
    await group_call.start(message.chat.id)


run = pytgcalls.start
