import sqlite3
createDB = sqlite3.connect('cmDB.db')
queryCurs = createDB.cursor()


def createTable():

    	queryCurs.execute('CREATE TABLE IF NOT EXISTS cm_table(id INTEGER PRIMARY KEY, username TEXT, phonenumber NUMBER)')

def add(username, phonenumber):

	queryCurs.execute('INSERT INTO cm_table (username, phonenumber) VALUES(?, ?)', (username, phonenumber))
	print "New contact added"

def read():
	#pass
	queryCurs.execute('SELECT * FROM cm_table WHERE username = "kate"')
	for row in queryCurs.fetchall():
		print(row)


#def data_entry():
		  
def main():
	createTable()
	add('cate', 07114)
	read()
	createDB.commit()

	



	

if __name__ == '__main__': main()