from telethon import TelegramClient, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 7396609
api_hash = '83a3c2a484499d8ca509fa995cb8722e'

client = TelegramClient('session_name', api_id, api_hash).start()

# Getting information about yourself
me = client.get_me()
print(me.stringify())

# Sending a message (you can use 'me' or 'self' to message yourself)
client.send_message(me, 'Hello World from Telethon!')
