import os

class sophiagaede:

	configVars = {
		"bot_account_id":"sophiagaede",

		# credentials
		"username":"sophiagaede@yahoo.com",
		"instagram_username":"sophiagaede",
		"password":"maria13", # don't use this password for other account in case they get hacked

		# timing
		"start_at_h":"07", # start program at hour MUST BE ZERO PADDED (eg. 09)
		"start_at_m":"00", # start program at minute MUST BE ZERO PADDED (eg. 09)
		"end_at_h":"20",	# End program at the hour MUST BE ZERO PADDED (eg. 09)
		"end_at_m":"00",	# End program at the min MUST BE ZERO PADDED (eg. 09)


		# limits
		"like_per_day":0, # likes per day
		"like_per_batch":0, # like per batch
		"comments_per_day":0, # Max Comments per day
		"follow_per_day":150, # people to follow per day
		"number_of_people_to_follow_per_user":10, # the number of people to follow per individual user I am scraping followers from
		"follow_time":3*24*60*60, # Seconds to wait before unfollowing
		"unfollow_per_day":150, # Max Users to unfollow per day
		"posts_per_day":0, # how many photos to post per day
		"post_backlog":0, # how many unposted, saved photos that are scheduled to be posted there should be on average
		"times_of_posts":[], # array of possible times to post pictures
		## NOTE:
		# follow_per_day should equal unfollow_per_day (unless you want to have more followers than unfollowers)
		# also your average follow count will be your follow_time (IN DAYS) multiplied by the number of people you follow per day
		# example: if you unfollow people after 4 days and follow 200 people a day, your average follower count will hover around 800

		# follow specific
		"follow_batches":6, # the amount of batches the total daily follower count should be broken up into
		"break_between_follow_batches":[1*60*60,3*60*60], # the [min,max] time between follow batch execution
		"unfollow_batches":6, # the amount of batches the total daily follower count should be broken up into
		"break_between_unfollow_batches":[1*60*60,3*60*60], # the [min,max] time between follow batch execution

		# accounts
		"account_to_scrape_followers_from":["life_miracle_j", "femkemegan", "girlcodewithbee", "sophievaneeuwijk", "arielledannique", "ingewagenmaker", "andreavandervoort", "lauvde", "elisetricarico", "anastasiya_panova", "febe.ampe", "emma.dbsr", "thedutchbandit", "ivamihovska", "annickkooiman", "louiisedam", "madalenaduartee", "justynalafayette", "giadacarrara", "jamie_fabulous", "daniquehoofwijk", "simonevangrinsven", "jasmijnmarcus", "sannebrusselaars", "annajirina", "vivianvandebunt"], # usernames of accounts to follow people from
		"accounts_to_scrape_posts_from":False,

		# emails
		"master_email":"feelfit.master@gmail.com", # email address to send emails to in case of: dialy reports, direct messages,
		"this_account_email":"feelfit.master@gmail.com", # email address of this account. The sender address for all emails in this bot
		"this_account_email_password":"f33lF!t59", # email password of this account

		# hashtags
		"hashtag_blacklist":False, # hashtags of pictures that should not be reposted
		"post_hashtag":False, # hashtags to add to posts

		# comments
		"captions": ["😍","😱","👑"],

		# proxy
		#proxy	str	Access instagram through a proxy. (host:port or user:password@host:port)
		"proxy":"",
		"use_proxy":False,

		# headless
		"headless":False, # setting headless to true will make the browser window not appear even if the bot is runnings
	}



