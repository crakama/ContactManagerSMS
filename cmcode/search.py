
class PhoneBookList(object):
	'''
	This class employs `list` datastructure in managing Phone contacts.

	'''
	def __init__(self):
	 	self.book = []
	def add_contact(self, Name, MobileNumber):

	 	record = [Name, MobileNumber] 
	 	self.book.append(record)
  

	def search(userinput):
		queryCurs.execute('SELECT * FROM cm_table WHERE username = "kate"')
		for row in queryCurs.fetchall():
			print row
			#count = 0
			#print row
		    
	   	    #count += 1
	   	    
	   	    	
	   	    #return result

b = PhoneBookList()
b.add_contact('kate', '883993')
b.add_contact('maggie', '883993')
b.add_contact('james', '883993')

#print b.book
#print b.search('kate')
userinput = input ("Please input value of x\n") 
print userinput
b.search(userinput)