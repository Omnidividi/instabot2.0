from bot.config.config import config
from bot.constants import constants
from bot.utilities.request.Request import Request
import datetime

class EvaluatePosts:

	def __init__(self):
		self.generateMessage()
		self.generateSubject()

	recipient = config().get("master_email")
	subject = ""
	message = ""
	attachmentAvailable = False

	def generateMessage(self):
		dailyStats = Request().get("/post/daily-stats").json()

		url = constants.base_website + "/evaluate/" + config().get("bot_account_id")
		postsScrapedTodayMessage = "{} posts were scraped today.".format(dailyStats["scrapedToday"])
		postBacklogMessage = "{} posts are in the backlog.".format(dailyStats["inBacklog"])
		postBacklogMessageAddon = "!!!!" if dailyStats["inBacklog"] < 10 else ""
		toBeApproved = "{} posts have yet to be approved.".format(dailyStats["toBeApproved"])
		
		messageText = """
		{}
		{} {}
		{}
		To evaluate posts, visit: {}
		"""
		finalMessage = messageText.format(postsScrapedTodayMessage, postBacklogMessage, postBacklogMessageAddon, toBeApproved, url)
		self.message = finalMessage

	def generateSubject(self):
		self.subject = "Daily Scraping Report For {}, for the {}".format(config().get("bot_account_id"), datetime.date.today() )