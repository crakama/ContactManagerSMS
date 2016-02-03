import sqlite3
createDB = sqlite3.connect('cmDB.db')
queryCurs = createDB.cursor()


def createTable():

    	queryCurs.execute('CREATE TABLE IF NOT EXISTS cm_table(id INTEGER PRIMARY KEY, username TEXT, phonenumber NUMBER)')

def add(username, phonenumber):

	queryCurs.execute('INSERT INTO cm_table (username, phonenumber) VALUES(?, ?)', (username, phonenumber))



#def data_entry():
		  
def main():
	createTable()
	add('cate', 07114)
	createDB.commit()

	queryCurs.execute( 'SELECT * FROM cm_table')

	for i in queryCurs:
		for j in i:
			print j


	

if __name__ == '__main__': main()