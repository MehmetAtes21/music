from pyrogram import Client, filters
from pyrogram.utils import MAX_CHANNEL_ID

from pytgcalls import GroupCallFactory

app = Client('pytgcalls')
group_call = GroupCallFactory(app).get_file_group_call('input.raw')


@group_call.on_network_status_changed
async def on_network_changed(context, is_connected):
    chat_id = MAX_CHANNEL_ID - context.full_chat.id
    if is_connected:
        await app.send_message(chat_id, 'Successfully joined!')
    else:
        await app.send_message(chat_id, 'Disconnected from voice chat..')


@app.on_message(filters.outgoing & filters.command('join'))
async def join_handler(_, message):
    await group_call.start(message.chat.id)


app.run()
