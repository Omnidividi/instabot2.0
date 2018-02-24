import os
from bot.constants import constants
import pickle

class config:

	configVars = {}

	# def __init__(self):
		

	def importConfigConstants(self):
		with open(constants.config_path, 'rb') as f:
			self.configVars = pickle.load(f)

	def get(self, key):
		self.importConfigConstants()
		return self.configVars[key]
		
	def setConfig(self, configClass):
		print("setting cofing")
		with open(constants.config_path, 'wb') as f:
			pickle.dump(configClass.configVars, f, pickle.HIGHEST_PROTOCOL)


	


	