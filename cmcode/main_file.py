import os
import sys

import sqlite3
createDB = sqlite3.connect('cmdb.db')
queryCurs = createDB.cursor()
class  Contacts(object):
    def __init__(self):

        self.contactdict = {}

    def createTable():

        queryCurs.execute('CREATE TABLE IF NOT EXISTS cmtable(id INTEGER PRIMARY KEY, name TEXT, lname TEXT, m_number NUMBER)')

    def add(name, m_number):

     queryCurs.execute('INSERT INTO cmtable (name, m_number) VALUES(?, ?)', (name, m_number))

     print "New contact added"





    def sendtext(num):
        queryCurs.execute('SELECT m_number FROM cmtable')
        result = queryCurs.fetchall()
        dictresult = dict(result)
        print dictresult
        instance = []
        #for k, v in dictresult.iteritems():
        for key in dictresult.iterkeys():
            #if key == name:
                instance.append(dictresult.get(key))
                print instance[0]
 

    def  searchname(name):   
        count = 0
        #lst = []
    #name = str (name)
        #print name
    #v = unicode(name)
        queryCurs.execute('SELECT name, m_number FROM cmtable')
        result = queryCurs.fetchall()
        dictresult = dict(result)

        instance = []
        #for k, v in dictresult.iteritems():
        for key in dictresult.iterkeys():
            if key == name:
                instance.append(dictresult.get(key))
                print instance[0]
 
                #instance.append(v)

        if len(instance) > 1:
            choice = None

            while choice is None:

                print("Which {} do you mean".format(name))

                for index, name in enumerate(instances):

                    print("[{}] {} {}".format(index, name, second_name))

                    choice = int(raw_input("> "))

                if choice not in range(len(instances)):

                    print("Wrong choice")

                    choice = None

            #for occur in instance:
                #print instance.append(dictresult.get(occur))
                #print occur

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
            add(name, m_number)
            createDB.commit()
            createDB.close()


        elif command == 'search':
            if len(args) != 1:
                print "Search Name is required"
                quit()
            name = args[0]
            searchname(name)
        elif command == 'text':
            if len(args) != 1:
            print "text Name and message is required"
                quit()
            name = args[0]
            searchname(name)

    
        else:
            print "Invalid command"