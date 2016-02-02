import sqlite3
createDB = sqlite3.connect('contactsDB.db')
queryCurs = createDB.cursor()
class Contacts(object):
	createDB = sqlite3.connect('contactsDB.db')
	queryCurs = createDB.cursor()

	def __init__(self):
	 	self.contactslst = {}

	def createTable():
		queryCurs.execute('CREATE TABLE IF NOT EXISTS cm_table(id INTEGER PRIMARY KEY, fname TEXT, phonenumber NUMBER)')
	
	def addcontact(self, fname, phonenumber):
		queryCurs.execute('''INSERT INTO cm_table (fname, phonenumber) VALUES(?, ?)''', (fname, phonenumber))
		createTable()

createDB.commit() 
queryCurs.close()
createDB.close()



