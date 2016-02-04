class PhoneBookDict(object):
	'''
	This class employs `dict` datastructure in managing Phone contacts.

	'''
	def __init__(self):
	 	self.book = {}
	def add_contact(self, username, phone_number):
	 	
	 self.book[username] = phone_number
	def search(self, username):
		#if username in self.book: / self.book.has_key(username)
		#	return
		#else: return
		return result

		result = {
	   	    	       'count': 1,
	   	    	       'phone_number': self.book.get(username, None) 
	   	    	}
	   	return result
	   	    	# a dictionary that has key (6) and value(9)

b = PhoneBookDict()
b.book["John"] = 938477566
b.book["Jack"] = 938377264
b.book["Jill"] = 947662781

print b.book

print b.search('kate')

