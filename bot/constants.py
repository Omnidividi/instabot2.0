import os

class constants:
	base_website="http://london-pt.co.uk"
	
	base_path=os.path.dirname(os.path.abspath(__file__))

	config_path =base_path + "/config/config.pkl"

	# headless
	headless=True # setting headless to true will make the browser window not appear even if the bot is runnings