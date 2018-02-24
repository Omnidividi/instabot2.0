import accounts
from bot import instaBot
from bot.config.config import config

for account in accounts.configs:
	print("{}: started at {}".format(account.name, now))
	instaBot.instaBot(account).dailyWrapUp()
	print("{}: ended at {}".format(account.name, now))
	for _ in range(3):
		print("----------------------------------------------------")

