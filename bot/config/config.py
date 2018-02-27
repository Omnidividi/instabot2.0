import os
from bot.constants import constants
import pickle

class config:

	configVars = {}

	# def __init__(self):

	def configConstants(self):
		return {
			"filedriver":"local",
			"local_path":constants.base_path + "/scrape/ScrapedImages/" + self.get("bot_account_id") + "/",
			"daily_vars_path":constants.base_path + "/daily/" + self.get("bot_account_id") + "/dailyVars.pkl",
			"log_path":constants.base_path + "/utilities/logger/" + self.get("bot_account_id") + "/errors.log",
			"session_path":constants.base_path + "/utilities/sessions/" + self.get("bot_account_id") + "/",
		}
		
		

	def importConfigConstants(self):
		with open(constants.config_path, 'rb') as f:
			self.configVars = pickle.load(f)

	def get(self, key):
		self.importConfigConstants()
		return self.configVars[key]

	def getConstant(self, key):
		myConstants = self.configConstants()
		return myConstants[key]
		
	def setConfig(self, configClass):
		with open(constants.config_path, 'wb') as f:
			pickle.dump(configClass.configVars, f, pickle.HIGHEST_PROTOCOL)


	


	