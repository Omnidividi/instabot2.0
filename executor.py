import accounts
from bot import instaBot
from bot.config.config import config
import datetime
from time import sleep
import random
from selenium import webdriver

class executor():

	def run(self, functionString, testing = False):
		self.testing = testing
		self.printSeperator("+", 3)

		if not self.testing:
			random.shuffle(accounts.configs)

		self.executeFunction(functionString)



	def now(self):
		currentDT = datetime.datetime.now()
		return currentDT.strftime("%Y-%m-%d %H:%M:%S")

	def printSeperator(self, character, rows = 1):
		stringToPrint = character * 40
		for _ in range(rows):
			print(stringToPrint)

	def executeFunction(self, functionString):
		for account in accounts.configs:

			print("{}: started at {}".format(account.configVars["bot_account_id"], self.now()))
			if not self.testing:
				sleep(random.randint(0, 3*60))
			print("{}: finished delay at {}".format(account.configVars["bot_account_id"], self.now()))

			if not account.configVars["active"]:
				print("{} account not active".format(account.configVars["bot_account_id"]))
				continue
			
			instabot = instaBot.instaBot(account)
			functionToCall = getattr(instabot, functionString)

			try:
				functionToCall()
			except Exception as e:
				print(e)
			finally:
				if instabot.browser != None:
					instabot.browser.quit()

			print("{}: ended at {}".format(account.configVars["bot_account_id"], self.now()))
			self.printSeperator("-")


### as randomisation measures we:
# 1. set a random delay
# 2. shuffle the array

