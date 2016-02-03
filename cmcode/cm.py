import sqlite3
from docopt import docopt, DocoptExit
import sys
import cmd
createDB = sqlite3.connect('cmDB.db')
queryCurs = createDB.cursor()



"""

Usage:
    cm.py add -n <name> -p <phonenumber> 
    cm.py (-h | --help | --version)
    cm.py (-i | --interactive)
Options:
    -h, --help  Show this screen and exit.
    -i, --interactive  Interactive Mode
"""


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
def fn(self, arg):
	try:
	 opt = docopt(fn.__doc__, arg)

	except DocoptExit as e:
 
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
     
            return

        return func(self, opt)
        fn.__name__ = func.__name__
        fn.__doc__ = func.__doc__
        fn.__dict__.update(func.__dict__)
        return fn

class Contacts (cmd.Cmd):
    intro = 'Manage your Contacts!' 
    prompt = 'cm'
    file = None

    @docopt_cmd
    def do_add(self, username, phonenumber):
        """Usage: add -n <name> -p <phonenumber>"""
    #sn = raw_input("Enter Name")
    #pn = raw_input("Enter Number")
       #if isinstace(str, sn) and isinstace(str, pn):
       	#print(sn)
       	#print(pn)
       	#username = sn
       #	phonenumber = pn
       #elif
        print "hjgjyg"
        queryCurs.execute('''INSERT INTO cm_table (username, phonenumber) VALUES(?, ?)''', (username, phonenumber))


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Done!')
        exit()
    def createTable():

    	queryCurs.execute('CREATE TABLE IF NOT EXISTS cm_table(id INTEGER PRIMARY KEY, username TEXT, phonenumber NUMBER)')
	

    def main():
	createTable()
	#Contacts().cmdloop()
	add(username, phonenumber)

	createDB.commit()
	if __name__ == '__main__': main()

	opt = docopt(__doc__, sys.argv[1:])

	if opt['--interactive']:
		Contacts().cmdloop()

		print(opt)