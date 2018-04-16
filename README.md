# parse-imessage-conversations
A couple of simple functions to extract data with python from conversations within the iMessage sqlite3 database from an iPhone. 

def get_row_id(num, path_to_db):
	""" Returns handle_id(s) which is a foreign key 
	
	num - Phone number or email formatted like: "+16018749522"
	"""
  
def get_messages_data(handle_id, path_to_db):
	""" Queries sqlite3 database and returns list of tuples containing messages info."""
  
def get_ngrams(text, gram):
	""" This returns a list of tuples of n-grams
	
	text - string of text (like returned from get_wikipedia_text()
	gram - int of the number of words in n-gram
	"""
  
def sort_ngrams_by_frequency(ngrams):
	""" This sorts ngrams by the ammount of times they appear
	
	ngrams - a list of tuples of ngrams like returned from get_ngrams
	"""
  
def get_sender_distribution(messages_data):
	"""
	Returns dict of distribution of num of messages sent by each person
	
	messages_data - tuple returned from get_messages_data()
	"""

def get_raw_text(messages_data):
	""" Returns dict, raw messages text from sender and reciever 
	
	messages_data - tuple returned from get_messages_data()
	"""
  
def get_date_distribution(messages_data):
	""" Returns list of tuples of (date: is_from_me)
	
	messages_data - tuple returned from get_messages_data()
	"""
