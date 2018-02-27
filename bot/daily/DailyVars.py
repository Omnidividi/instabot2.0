from random import randrange
import time
import datetime
from datetime import timedelta
from bot.config.config import config
import pickle
import os

class DailyVars:

	def filePath(self):
		return config().getConstant("daily_vars_path")

	def __init__(self):
		try:
			self.vars = self.load_obj()
		except (OSError, IOError) as e:
			print("error 1")
			self.generateNewVars()
			self.vars = self.load_obj()

		if self.vars["date"] != self.today():
			self.generateNewVars()
			self.vars = self.load_obj()


	def today(self):
		return datetime.datetime.today().strftime('%Y-%m-%d')

	def save_obj(self, obj):
		directoryPath = self.filePath().replace("/dailyVars.pkl","")

		if not os.path.exists(directoryPath):
			os.makedirs(directoryPath)

		try:
			file = open(self.filePath(), 'wb')
		except OSError:
			file = open(self.filePath(), 'w')
			
		pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)

		# with open(self.filePath(), 'wb') as f:
		# 	pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

	def load_obj(self):
	    with open(self.filePath(), 'rb') as f:
	        return pickle.load(f)

	def generateNewVars(self):
		dailyTimes = {
			"vars": {
				"follow": [],
				"unfollow": [],
				"post": [],
				"like": [],
			},
			"date": self.today(),
		}

		for _ in range(config().get("follow_batches")):
			dailyTimes["vars"]["follow"].append({"complete": 0, "time": self.random_date()})

		for _ in range(config().get("unfollow_batches")):
			dailyTimes["vars"]["unfollow"].append({"complete": 0, "time": self.random_date()})

		for _ in range(config().get("posts_per_day")):
			dailyTimes["vars"]["post"].append({"complete": 0, "time": self.random_date()})
		if not (config().get("like_per_day") == 0 and config().get("like_per_batch") == 0):
			likeBatches = int(round(config().get("like_per_day")/config().get("like_per_batch")))
			for _ in range(likeBatches):
				dailyTimes["vars"]["like"].append({"complete": 0, "time": self.random_date()})

		self.save_obj(dailyTimes)


	def random_date(self):
		todayYMD = datetime.datetime.today().strftime('%Y-%m-%d')
		start = todayYMD + " " + config().get("start_at_h") + ":" + config().get("start_at_m")
		end = todayYMD + " " + config().get("end_at_h") + ":" + config().get("end_at_m")
		start_timestamp = time.mktime(time.strptime(start, '%Y-%m-%d %H:%M'))
		end_timestamp = time.mktime(time.strptime(end, '%Y-%m-%d %H:%M'))
		randomTime = time.strftime('%Y-%m-%d %H:%M', time.localtime(randrange(start_timestamp,end_timestamp)))

		return randomTime

	def should(self, key):
		times = self.vars["vars"][key]
		nonCompletedTimes = [time['time'] for time in times if time['complete'] == 0]
		if len(nonCompletedTimes) == 0:
			return False
			
		earliestNonCompleted = min(nonCompletedTimes)
		nowStrToTime = time.time()
		nowString = datetime.datetime.fromtimestamp(nowStrToTime).strftime('%Y-%m-%d %H:%M')

		if earliestNonCompleted <= nowString:
			[var.update({"complete" : 1}) for var in self.vars["vars"][key] if var["time"] == earliestNonCompleted]
			self.save_obj(self.vars)
			return True
		else:
			return False
		# get earliest
		# see if earlier than now
			# if it is then return true and set complete to 1
		# else
			# return
		





