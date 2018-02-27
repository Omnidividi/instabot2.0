from selenium import webdriver
from time import sleep
from bot.scrape.Scraper import Scraper
from bot.scrape.Handlers.UserScraper import UserScraper
from bot.login.AutoLogin import AutoLogin
from bot.post.Poster import Poster
from bot.follow.FollowManager import FollowManager
from bot.daily.Daily import Daily
from bot.config.config import config
from bot.daily.DailyVars import DailyVars
from bot.utilities.logger.MyLogger import MyLogger
from bot.utilities.request.Request import Request
from bot.engagement.ActionsOnHomepage import ActionsOnHomepage
from bot.follow.FollowExceptions import FollowExceptions
from bot.constants import constants
from selenium.webdriver.common.proxy import Proxy
import datetime
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class instaBot:

	def __init__(self, account):
		config().setConfig(account)
		print(config().get("bot_account_id"))
		self.browser = None
		self.dailyVars = DailyVars()

	def instantiateBrowser(self):

		if self.browser == None:
			chrome_options = webdriver.ChromeOptions()
			mobile_emulation = { "deviceName": "iPhone 7" }
			chrome_options = webdriver.ChromeOptions()
			chrome_options.add_argument('--no-sandbox')
			chrome_options.add_argument("--disable-setuid-sandbox")
			chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
			chrome_options.add_argument('--disable-extensions')
			chrome_options.add_argument('--no-sandbox')

			path = config().getConstant("session_path")
			chrome_options.add_argument("user-data-dir={}".format(path))

			if constants.headless:
				chrome_options.add_argument('--headless')
				chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary.


			capabilities = DesiredCapabilities.CHROME
			if config().get("use_proxy"):
				print("using proxy")
				proxy_address = config().get("proxy_address")
				proxy = Proxy()
				proxy.socksPassword = config().get("proxy_password")
				proxy.socksUsername = config().get("proxy_username")
				proxy.ftpProxy = proxy_address
				proxy.httpProxy = proxy_address
				proxy.sslProxy = proxy_address
				proxy.proxy_type = {'ff_value': 1, 'string': 'MANUAL'}
				proxy.add_to_capabilities(capabilities)
				
			else:
				capabilities.pop('proxy', None)
			
			self.browser = webdriver.Chrome(chrome_options=chrome_options,desired_capabilities=capabilities)

			if True: ## checking ip address
				print(capabilities)
				# print("screenshot")
				# self.browser.get("https://whatismyipaddress.com/")
				# self.browser.save_screenshot(config().get("bot_account_id") + ".png")


			AutoLogin(self.browser).login()


	def scrapingIncomplete(self):
		postBacklogAmount = Request().get("/post/backlog/amount").json()
		return postBacklogAmount < config().get("post_backlog")

	def run(self):

		if self.scrapingIncomplete():
			self.instantiateBrowser()
			scraper = Scraper(UserScraper(self.browser))
			scraper.run()


		if self.dailyVars.should("follow"):
			print("should follow true")
			self.instantiateBrowser()
			followManager = FollowManager(self.browser)
			try:
				followManager.follow()
			except FollowExceptions.InstagramBlocksFollow: 
				print("blocked follow")
			

		if self.dailyVars.should("unfollow"):
			print("should unfollow true")
			self.instantiateBrowser()
			followManager = FollowManager(self.browser)
			followManager.unfollow()
		# if self.dailyVars.should("like"):
		# 	self.instantiateBrowser()
		# 	actionsOnHomepage = ActionsOnHomepage(self.browser)
		# 	actionsOnHomepage.like(config().get("like_per_batch"))
			

		if self.dailyVars.should("post"):
			MyLogger().log("should post true")
			self.instantiateBrowser()
			poster = Poster(self.browser)
			poster.run()


		return


		# except:
		# 	print("critical error, no user with good posts could be found")
		# do login
		# do likes
		# do follows
		# do unfollows
		# do posts
		# do comments

	def dailyWrapUp(self):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument("--disable-setuid-sandbox")
		chrome_options.add_argument('--disable-extensions')
		chrome_options.add_argument('--no-sandbox')

		if constants.headless:
			chrome_options.add_argument('--headless')
			chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary.


		capabilities = DesiredCapabilities.CHROME
		if "procxy" != capabilities:
			capabilities.pop('proxy', None)
		
		print(capabilities)
		self.browser = webdriver.Chrome(chrome_options=chrome_options,desired_capabilities=capabilities)

			
		dailyHandler = Daily(self.browser)
		# # send email to self with information about scraped posts, post backlog and post evaluation
		dailyHandler.evaluatePosts()
		# # send email to self about daily statistics and report to database the follower and following count
		dailyHandler.dailyReport()
		# # send email to self about errors that occured today
		dailyHandler.reportErrors()
		# delete all images that have been posted or disapproved to save space
		dailyHandler.cleanOutScrapedImages()

		return







# to do

	# a function where it finds special posts for special days
		# eg. cheat day sunday - account finds cheat meal picture on saturday to post for sunday
	# video repost function
	# wait wait wait - instead of saving picture, why dont I just use the web_url to repost???????????
	# check likes on posts to repost to find the most popular
	# before saving a post, check if database has already saved it
	# manual submission of a post - the post is added to the database and to the scraped images
	# maybe also make mechanism to delete all the hastags off old posts - with fewer hashtags they look more legit
	# write script to handle if a bot gets to a page and it says the user is not available like: https://www.instagram.com/aurora_LZ_Fit/
	# go through and delete all the sleeps
	# MyLogger all errors
	# Upload and update from github so that all the projects are always consistant
	# do it so that the browser only opens and logs in if a task is really to be performed - otherwise if instagram is logged
	# into consistantly every hour, at the same time, instagram will get suspicious
	# make MyLogger log to a different file than the automatic error logger - errors.log is very hard to read
	# make it so that scrapper recognises whether a post is eligible for scraping (except for the hashtag criteria) before clicking on it





