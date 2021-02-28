from .. import loader, utils 
from telethon import events

def register(cb):
    cb(HahahaMod())

class HahahaMod(loader.Module):
	"""Хахахаталка от @OfficialShina. Использование: .ha <кол-во> (от 1 до 350) """
	strings = {'name': 'Hahaha'}
	async def hacmd(self, message):
		args = utils.get_args_raw(message)
		if args.isdigit():
			if int(args) <= 350:
				haha = "ХА"*int(args)
				reply = await message.get_reply_message()
				if reply:
					await message.delete()
					await reply.reply(haha)
				else:
					await message.delete()
					await message.respond(haha)		 
			else:
				await message.delete()
				await message.respond('ХА'*350)
		else:
			await message.delete()
			await message.respond('ХА')
