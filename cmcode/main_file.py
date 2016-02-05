import os
import sys
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
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





    def sendtext(num, msg):

        queryCurs.execute('SELECT name, m_number FROM cmtable')

        result = queryCurs.fetchall()

        dictresult = dict(result)

        # print dictresult

        instance = []
        #for k, v in dictresult.iteritems():
        for key in dictresult.iterkeys():
            #if key == name:
            instance.append(str(dictresult.get(key)))

        contactlist = ",".join((instance))
        #print contactlist
        return contactlist

    def  searchname(name):   
        count = 0

        queryCurs.execute('SELECT name, m_number FROM cmtable')
        result = queryCurs.fetchall()
        dictresult = dict(result)

        instance = []
        #for k, v in dictresult.iteritems():
        for key in dictresult.iterkeys():
            if key.lower() == name.lower():

                instance.append(str(dictresult.get(key)))

                #print instance[0]
                return instance[0]
     

        if len(instance) > 1:
            choice = None

            while choice is None:

                print("Which {} do you mean".format(name))

                for index, name in enumerate(instance):

                    print("[{}] {} {}".format(index, name, lname))

                    choice = int(raw_input("> "))

                if choice not in range(len(instance)):

                    print("Wrong choice")

                    choice = None
            print choice

            #raw_input("Which %s" % (name))


    def main():
        pass

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


        elif command == 'lookup':
            if len(args) != 1:
                print "Search Name is required"
                quit()
            name = args[0]
            searchname(name)

        elif command == 'text':
            if len(args) != 2:
                print "text Name and message is required"
                quit()
            name = args[0]
            message = args[1]
            sendtext(name, message)

    
        else:
            print "Invalid command"
