import os

class constants:
	base_website="http://london-pt.co.uk"
	
	base_path=os.path.dirname(os.path.abspath(__file__))
	# filedriver options
	filedriver="local"
	local_path=base_path + "/scrape/ScrapedImages/"
	# logging options
	log_path=base_path + "/utilities/logger/errors.log"

	config_path =base_path + "/config/config.pkl"

	# headless
	headless=False # setting headless to true will make the browser window not appear even if the bot is runnings



