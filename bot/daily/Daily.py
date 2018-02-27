from bot.utilities.email.EmailDriver import Email
from bot.utilities.email.EmailVariants.EvaluatePosts import EvaluatePosts
from bot.utilities.email.EmailVariants.DailyReport import DailyReport
from bot.utilities.logger.MyLogger import MyLogger
from bot.config.config import config
from bot.utilities.request.Request import Request
from json.decoder import JSONDecodeError
from bot.utilities.filedriver.Local import Local

class Daily:

	def __init__(self, browser):
		self.browser = browser

	def evaluatePosts(self):
		Email(EvaluatePosts()).send()

	def dailyReport(self):
		self.browser.get("https://www.instagram.com/" + config().get("instagram_username") + "/")
		followerAndFollowingCount = self.browser.find_element_by_css_selector("ul._h9luf li span._fd86t")
		followerCount = followerAndFollowingCount[1].text.replace(",","")
		followingCount = followerAndFollowingCount[2].text.replace(",","")

		# followerCount = self.browser.find_element_by_css_selector("a[href*='followers'] span").text.replace(",","")
		# followingCount = self.browser.find_element_by_css_selector("a[href*='following'] span").text.replace(",","")
		print(followerCount)
		print(followingCount)

		Request().post("/report/follower-count", {"followerCount": followerCount, "followingCount": followingCount})

		Email(DailyReport(followerCount, followingCount)).send()

	def reportErrors(self):
		MyLogger().send()
		MyLogger().empty()

	def cleanOutScrapedImages(self):
		local = Local()
		try:
			# fetch images that have been disapproved or that have been posted
		    filepaths = Request().get("/post/can-be-deleted").json()
		    for filepath in filepaths:
		     	# check if the images exist in scraped images and delete them
		    	local.deleteIfExists(filepath)

		except JSONDecodeError:
		    print("no posts to delete")



