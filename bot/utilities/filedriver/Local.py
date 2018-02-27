import urllib
from bot.scrape.ScrapeExceptions import ScrapeExceptions
import os
from bot.config.config import config
from pathlib import Path
from bot.utilities.logger.MyLogger import MyLogger

class Local:

	#### move this to saveLocation
	def download(self, postInstance):
		self.createScrapedImageDirectoryForThisAccountIfItDoesNotExist()
		try:
			imagePath = config().getConstant("local_path") + postInstance.instaId + ".jpg"
			urllib.request.urlretrieve(postInstance.imageUrl, imagePath)
			return postInstance.instaId
		except Exception as e:
			MyLogger().log(e)
			raise ScrapeExceptions.FileSaveError()

	def createScrapedImageDirectoryForThisAccountIfItDoesNotExist(self):
		directoryPath = config().getConstant("local_path")

		if not os.path.exists(directoryPath):
			os.makedirs(directoryPath)
		
	def get(self, filePath):
		return config().getConstant("local_path") + filePath + ".jpg"

	def deleteIfExists(self, filePath):
		fullFilePath = config().getConstant("local_path") + filePath + ".jpg"
		if os.path.exists(fullFilePath):
			os.remove(fullFilePath)
    