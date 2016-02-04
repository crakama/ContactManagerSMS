 queryCurs.execute('SELECT name, m_number FROM cmtable')
        result = queryCurs.fetchall()
        dictresult = dict(result)

        instance = []
        #for k, v in dictresult.iteritems():
        for key in dictresult.iterkeys():
            if key == name:
                instance.append(dictresult.get(key))
                print instance[0]
 