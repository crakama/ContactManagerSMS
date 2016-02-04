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

	 ''' returns a `dict` with phone_number and number of loop count e.g {'count': 'austin', 'phone_number'}'''
	     return result
	     result = {
	   	    	       'count': 1,
	   	    	       'phone_number': self.book.get(username, None) 
	   	    	}
	 return result
	   	    	# a dictionary that has key (6) and value(9)

b = PhoneBookDict()
b.add_contact('kate', '883993')
b.add_contact('maggie', '883993')
b.add_contact('james', '883993')

print b.book

print b.search('kate')

b.phonebook["John"] = 938477566
b.phonebook["Jack"] = 938377264
b.phonebook["Jill"] = 947662781