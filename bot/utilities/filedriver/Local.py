import urllib
from bot.scrape.ScrapeExceptions import ScrapeExceptions
import os
from bot.constants import constants
from pathlib import Path
from bot.utilities.logger.MyLogger import MyLogger

class Local:

	#### move this to saveLocation
	def download(self, postInstance):
		try:
			imagePath = constants.local_path + postInstance.instaId + ".jpg"
			urllib.request.urlretrieve(postInstance.imageUrl, imagePath)
			return postInstance.instaId
		except Exception as e:
			MyLogger().log(e)
			raise ScrapeExceptions.FileSaveError()
		
	def get(self, filePath):
		return constants.local_path + filePath + ".jpg"

	def deleteIfExists(self, filePath):
		fullFilePath = constants.local_path + filePath + ".jpg"
		if os.path.exists(fullFilePath):
			os.remove(fullFilePath)
    