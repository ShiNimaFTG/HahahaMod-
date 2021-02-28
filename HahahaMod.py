from .. import loader, utils 
from telethon import events

def register(cb):
    cb(HahahaMod())

class HahahaMod(loader.Module):
	"""Хахахаталка от @OfficialShina. Использование: .ha <кол-во>"""
	strings = {'name': 'Hahaha'}
	async def hacmd(self, message):
		args = utils.get_args_raw(message)
		if args.isdigit():
			haha = "ХА"*int(args)
			reply = await message.get_reply_message() 
			if reply:
				await message.delete()
				await reply.reply(haha)
			else:
				await message.delete()
				await message.respond(haha)
		else:
			message.respond('Чел, ты....')
			
