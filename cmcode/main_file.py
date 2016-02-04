import os
import sys

import sqlite3
createDB = sqlite3.connect('cmdb.db')
queryCurs = createDB.cursor()
class  Contacts(object):
    def __init__(self):

        self.contactdict = {}

    def createTable():

        queryCurs.execute('CREATE TABLE IF NOT EXISTS cmtable(id INTEGER PRIMARY KEY, name TEXT, m_number NUMBER)')

    def add(name, m_number):

     queryCurs.execute('INSERT INTO cmtable (name, m_number) VALUES(?, ?)', (name, m_number))

     print "New contact added"

    def  searchname(name):   
        count = 0
        #lst = []
    #name = str (name)
        print name
    #v = unicode(name)
        queryCurs.execute('SELECT name, m_number FROM cmtable')
        result = queryCurs.fetchall()
        dictresult = dict(result)

        instance = []
        for k, v in dictresult.iteritems():
            if v == name:

                instance.append(v)

        if instance > 1:
            for occur in instance:
                print occur

            raw_input("Which %s" % (name))

        
        #queryCurs.close()

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
                print "Name, number, required"
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
            name = args[0]
            searchname(name)

    
        else:
            print "Invalid command"