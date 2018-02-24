from bot.config.config import config
from bot.follow.FollowExceptions import FollowExceptions
from bot.follow.AutoFollow import AutoFollow
from bot.follow.AutoUnfollow import AutoUnfollow
from time import sleep
from bot.utilities.request.Request import Request
import random

class FollowManager:

	def __init__(self, browser):
		self.browser = browser
		self.AutoFollow = AutoFollow(self.browser)
		self.AutoUnfollow = AutoUnfollow(self.browser)

	def follow(self):
		self.usersWhoHaveHadFollowersStolen = []
		numberOfUsersToFollow = self.numberOfUsersToActuallyFollow()
		currentBatchSize = 0
		while currentBatchSize < numberOfUsersToFollow:
			peopleLeftToFollow = (numberOfUsersToFollow - currentBatchSize)
			followFromThisUserLimit = config().get("number_of_people_to_follow_per_user") if ((currentBatchSize + config().get("number_of_people_to_follow_per_user")) < numberOfUsersToFollow) else peopleLeftToFollow
			currentBatchSize += followFromThisUserLimit
			try:
				username = self.unscrapedUserToStealFollowersFrom()
				self.AutoFollow.followFromUser(username, followFromThisUserLimit)
			except FollowExceptions.NoMoreAccountsToStealFollowersFrom:
				break
			except FollowExceptions.UsernameDoesNotExist:
				continue


	def numberOfUsersToActuallyFollow(self):
		response = Request().get("/report/daily-report/fetch")
		usersFollowedToday = response.json()["followed"]
		usersToFollowTillLimit = config().get("follow_per_day") - usersFollowedToday

		usersToFollowPerBatch = (config().get("follow_per_day") / config().get("follow_batches"))

		return min(usersToFollowTillLimit, usersToFollowPerBatch)

	def unscrapedUserToStealFollowersFrom(self):
		userToStealFollowersFrom = config().get("account_to_scrape_followers_from")
		unscrapedUserToStealFollowersFrom = list(set(userToStealFollowersFrom) - set(self.usersWhoHaveHadFollowersStolen))
		random.shuffle(unscrapedUserToStealFollowersFrom)
		# check if there are any users left
		if len(unscrapedUserToStealFollowersFrom) == 0:
			raise FollowExceptions.NoMoreAccountsToStealFollowersFrom()
		# take first user
		randomUsername = unscrapedUserToStealFollowersFrom[0]
		# record and return random user
		self.usersWhoHaveHadFollowersStolen.append(randomUsername)
		return randomUsername






	def unfollow(self):
		usersToUnfollow = self.usersToUnfollow()
		self.AutoUnfollow.usersToUnfollow(usersToUnfollow)


	def usersToUnfollow(self):
		response = Request().post("/users-to-unfollow", {"unfollowUsersAfter": config().get("follow_time")})
		allUsersToUnfollow = response.json()
		numberOfUsersToActuallyUnfollow = self.numberOfUsersToActuallyUnfollow()

		allUsersToUnfollowLength= len(allUsersToUnfollow)
		numberOfUsersToActuallyUnfollow = numberOfUsersToActuallyUnfollow if numberOfUsersToActuallyUnfollow < allUsersToUnfollowLength else allUsersToUnfollowLength
		return allUsersToUnfollow[:numberOfUsersToActuallyUnfollow]

	def numberOfUsersToActuallyUnfollow(self):
		response = Request().get("/report/daily-report/fetch")
		usersUnfollowedToday = response.json()["unfollowed"]
		usersToUnfollowTillLimit = config().get("unfollow_per_day")

		usersToUnfollowPerBatch = (config().get("unfollow_per_day") / config().get("unfollow_batches"))

		return int(min(usersToUnfollowTillLimit, usersToUnfollowPerBatch))


