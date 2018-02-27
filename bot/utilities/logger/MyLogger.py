import logging
from bot.utilities.email.EmailDriver import Email
from bot.utilities.email.EmailVariants.ErrorLogEmail import ErrorLogEmail
from bot.config.config import config
import os

class MyLogger:


	def __init__(self):
		self.createLogDirectoryForThisAccountIfItDoesNotExist()
			
		logging.basicConfig(filename=config().getConstant("log_path"),level=logging.DEBUG)
		stream_handler = logging.StreamHandler()
		formatter = logging.Formatter("%(levelname)s : %(pathname)s:%(lineno)s - %(msg)s --- %(asctime)s")
		stream_handler.setFormatter(formatter)

		logger = logging.getLogger('foo')
		logger.addHandler(stream_handler)
		logger.setLevel(logging.DEBUG)

	def createLogDirectoryForThisAccountIfItDoesNotExist(self):
		directoryPath = config().getConstant("log_path").replace("/errors.log","")

		if not os.path.exists(directoryPath):
			os.makedirs(directoryPath)

		try:
			file = open(config().getConstant("log_path"), 'wb')
		except OSError:
			file = open(config().getConstant("log_path"), 'w')

	def log(self, error):
		logging.error("\n --------------------------------- \n", exc_info=True)
		logging.error(error, exc_info=True)
		logging.error("\n --------------------------------- \n", exc_info=True)

	def empty(self):
		with open(config().getConstant("log_path"), "w") as file:
			file.truncate()

	def send(self):
		Email(ErrorLogEmail()).send()
