from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputAudioStream, InputStream

from config import API_HASH, API_ID, SESSION_NAME
from callsmusic import queues

client = Client(SESSION_NAME, API_ID, API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update) -> None:
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.change_stream(
            InputStream(
                InputAudioStream(
                    queues.get(chat_id)["file"],
                ),
            ),
        )


run = pytgcalls.start
