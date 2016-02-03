import sqlite3
import argparse
createDB = sqlite3.connect('contactsDB.db')
queryCurs = createDB.cursor()

class Contacts(object):
	createDB = sqlite3.connect('contactsDB.db')
	queryCurs = createDB.cursor()

	def __init__(self):
	 	self.contactslst = {}

	def createTable():
		queryCurs.execute('CREATE TABLE IF NOT EXISTS cm_table(id INTEGER PRIMARY KEY, fname TEXT, phonenumber NUMBER)')
	
	def addcontact(self, name, phonenumber):
		queryCurs.execute('''INSERT INTO cm_table (fname, phonenumber) VALUES(?, ?)''', (fname, phonenumber))
		createTable()

createDB.commit() 
queryCurs.close()
createDB.close()

'''arglen = len(sys.argv)

if arglen == 2:
	
	nm = sys.argv[1][1] #reads second argument which is -n name
	pn = sys.argv[1][1][1]#reads second argument which is -p phonenumber
	nm = nm.lower()
	if nm == 'n': #then prompt the user to enter name
		   nw_name = raw_input('Enter Name:')

		   if isinstance(nw_name, str):
		   
		   	addContact(name, nw_name)
		   elif pn == 'p':
		   	nw_number = raw_input('Enter Number:')

		   if isinstance(nw_number, str):
		   
		   	addContact(name, nw_number)'''
    # Construct the arguments parser
    ag = argparse.ArgumentParser() #converts to dict

    # Parse the commandline arguments
    # Includes input file, output file and the seed.
    ag.add_argument('-n', action = 'nameaction', dest = 'Name' required=False, help="Enter Name")
    ag.add_argument('-p', action = 'phonenumber', required=False, help="Enter phonenumber")
    
    args = vars(ag.parse_args()) 


