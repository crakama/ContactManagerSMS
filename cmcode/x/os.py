import os
import sys

import sqlite3
createDB = sqlite3.connect('cmdb.db')
queryCurs = createDB.cursor()


def createTable():

    queryCurs.execute('CREATE TABLE IF NOT EXISTS cmtable(id INTEGER PRIMARY KEY, name TEXT, m_number NUMBER)')
    pass


def add(name, m_number):
    """Add a new name and number to the given phonebook.
    Args:
        name (str): name of the entry to add
        number (str): phone number of the entry to add
       
    """
    
    queryCurs.execute('INSERT INTO cmtable (name, m_number) VALUES(?, ?)', (name, m_number))
    print "New contact added"
    lines = 0
    lst = list()
    #name = str (name)
    #print name
    v = unicode(name)
    queryCurs.execute('SELECT * FROM cmtable WHERE name =(?)', (v, ) )
    print "fetchall:"
    result = queryCurs.fetchall() 
    print result
    for r in result:
        lst.append(r)
        lines += 1
        print(r)
        db.close()

def main():
    pass
    #createTable()

    #add('cate', 07114)
    #read()
    #createDB.commit()
if __name__ == '__main__': 
    main()
    args = sys.argv[:]
    script = args.pop(0)    # name of script is first arg
    if not args:
        print "Command required"
        quit()
    command = args.pop(0)   # the next arg will be the main command

    if command == 'add':
        if len(args) != 2:
            print "Name, number, and phonebook name required"
            quit()
        name, m_number = args
        createTable()
        add_entry(name, m_number)
        createDB.commit()
        createDB.close()


    elif command == 'search':
        if len(args) != 1:
            print "Search Name is required"
            quit()
        name = args
        searchname(name)

    
    else:
        print "Invalid command"