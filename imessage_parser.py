import sqlite3

def get_row_id(num, path_to_db):
	""" Returns handle_id(s) which is a foreign key 
	
	num - Phone number or email formatted like: "+16018749522"
	"""
	connection = sqlite3.connect(f"{path_to_db}")
	cursor = connection.cursor()
	query = f'select rowid, service from handle where id="{num}";'
	cursor.execute(query)

	return cursor.fetchall()

def get_messages_data(handle_id, path_to_db):
	""" Queries sqlite3 database and returns list of tuples containing messages info."""
	
	connection = sqlite3.connect(f"{path_to_db}")
	cursor = connection.cursor()
	query = f"""
	select
		is_from_me,
		datetime(date/1000000000 + strftime('%s','2001-01-01'), 'unixepoch') as date_utc,
		text
	from message 
	where handle_id={handle_id};
	"""
	cursor.execute(query)
	return cursor.fetchall()
	
def get_ngrams(text, gram):
	""" This returns a list of tuples of n-grams
	
	text - string of text (like returned from get_wikipedia_text()
	gram - int of the number of words in n-gram
	"""
	
	ngrams = []
	list_of_text = text.split()
	
	for x in (range(len(list_of_text) - (gram - 1))):
		
		trigram = ()
		
		for n in range(gram):
			trigram += (list_of_text[x+n],) #This MUST have a leading comma because you can only add tuples to tuples
		
		ngrams.append(trigram)
		
	return ngrams
	
def sort_ngrams_by_frequency(ngrams):
	""" This sorts ngrams by the ammount of times they appear
	
	ngrams - a list of tuples of ngrams like returned from get_ngrams
	"""
	
	counts = []
	
	for x in ngrams:
		
		if not [ngrams.count(x), x] in counts:
			counts.append([ngrams.count(x), x])
			
	return list(reversed(sorted(counts)))

def get_sender_distribution(messages_data):
	"""
	Returns dict of distribution of num of messages sent by each person
	
	messages_data - tuple returned from get_messages_data()
	"""
	
	user = 0
	other = 0
	for m in messages_data:
		if m[0]:
			user += 1
		else:
			other += 1
	return {"from_user": user, "from_other": other}
	
def get_raw_text(messages_data):
	""" Returns dict, raw messages text from sender and reciever 
	
	messages_data - tuple returned from get_messages_data()
	"""
	
	user_msgs = ""
	other_msgs = ""
	
	for m in messages_data:
		if m[2]:
			if m[0]:
				user_msgs += m[2] + " "
			else:
				other_msgs += m[2] + " "
			
	return {"from_user": user_msgs, "from_other": other_msgs}

def get_date_distribution(messages_data):
	""" Returns list of tuples of (date: is_from_me)
	
	messages_data - tuple returned from get_messages_data()
	"""
	dates = list()
	
	for m in messages_data:
		dates.append((m[1], True if m[0] else False))

	return dates
	
