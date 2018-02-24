from bot.scrape.ScrapeExceptions import ScrapeExceptions
from bot.config.config import config
from bot.utilities.request.Request import Request
from bot.utilities.logger.MyLogger import MyLogger

class Scraper:

	def __init__(self, scrapingHandler):
		self.scrapingHandler = scrapingHandler


	def run(self):
		while self.scrapingIncomplete():
			try:
				self.scrapingHandler.run()
			except ScrapeExceptions.NotEnoughPostsFound:
				break
				# LOG: log error to file

	def scrapingIncomplete(self):
		postBacklogAmount = Request().get("/post/backlog/amount").json()
		return postBacklogAmount < config().get("post_backlog")