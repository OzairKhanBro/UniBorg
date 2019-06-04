from telethon import events
from uniborg.util import admin_cmd
@borg.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
	try:
		# print("reciving message")
		# await event.send_message("me", event.message.text)
		if event.sender_id == 772528607 and "#SID" in event.message.text:  # autobot
			await event.message.click(0)
			# await event.send_message("me", event.message.text)

	# await event.message.reply("Hi i am there")
	except Exception:
		print("Exception")
