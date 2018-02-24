from bot.config.config import config
from bot.constants import constants
import datetime

class ErrorLogEmail:

	def __init__(self):
		self.generateMessage()
		self.generateSubject()
		self.generateAttachment()

	recipient = config().get("master_email")
	subject = ""
	message = ""
	attachmentAvailable = True

	def generateMessage(self):
		self.message = "Error log for {}".format(datetime.date.today())

	def generateSubject(self):
		self.subject = "Error log For {}, for the {}".format(config().get("bot_account_id"), datetime.date.today())

	def generateAttachment(self):
		self.attachmentName = "error.txt"
		self.attachment = constants.log_path