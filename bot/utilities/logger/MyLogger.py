import logging
from bot.utilities.email.EmailDriver import Email
from bot.utilities.email.EmailVariants.ErrorLogEmail import ErrorLogEmail
from bot.constants import constants

class MyLogger:


	def __init__(self):
		logging.basicConfig(filename=constants.log_path,level=logging.DEBUG)
		stream_handler = logging.StreamHandler()
		formatter = logging.Formatter("%(levelname)s : %(pathname)s:%(lineno)s - %(msg)s --- %(asctime)s")
		stream_handler.setFormatter(formatter)

		logger = logging.getLogger('foo')
		logger.addHandler(stream_handler)
		logger.setLevel(logging.DEBUG)



	def log(self, error):
		logging.error("\n --------------------------------- \n", exc_info=True)
		logging.error(error, exc_info=True)
		logging.error("\n --------------------------------- \n", exc_info=True)

	def empty(self):
		with open(constants.log_path, "w") as file:
			file.truncate()

	def send(self):
		Email(ErrorLogEmail()).send()
