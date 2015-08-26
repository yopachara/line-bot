#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json, codecs, httplib, urllib

from pprint import pprint

#with open('/usr/local/lib/python2.7/site-packages/line/Persons.json') as data_file:
#    data = json.load(data_file)


#my_data = json.loads(open('/usr/local/lib/python2.7/site-packages/line/Persons.json').read())

#print pprint(data)
#with open('/usr/local/lib/python2.7/site-packages/line/Persons.json') as data_file:
#    data = json.loads(data_file.read().decode('UTF-8'))
#output_file = codecs.open('/usr/local/lib/python2.7/site-packages/line/Persons.json','W',encoding='utf-8')

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('GET', '/1/classes/Persons', '', {
       "X-Parse-Application-Id": "rt696aIikdtgzI2XVPFaOBrydo0ZQKKsuBu3VoEM",
       "X-Parse-REST-API-Key": "9gZZ1zsxw5Aiu2dqvfXcwnZ4F9YVmJS4Jdw7XP2l"
     })
result1 = json.dumps(connection.getresponse().read())
print result1
results = result1['results']
results = results.decode('utf-8')

#print pprint(results[5])
print pprint(results)

def search(name):
    for result in results:
        #print results
        name = name.decode('utf-8')
        print name
        #name = name
        if (result['fname'] in name or
            result['facebook'] in name or
            result['lname'] in name or
            result['nickname'] in name or
            result['position'] in name):
            # address_component['long_name'] and
            # address_component['short_name'] are your data
            rt =  '%s %s (%s)\n%s \n %s %s'%(result['fname'],result['lname'],result['nickname'],result['phone'],result['lineID'],result['email'])
            print '%s %s (%s)\n%s \n %s %s'%(result['fname'],result['lname'],result['nickname'],result['phone'],result['lineID'],result['email'])
            return rt
            break
msg = 'asdasd asdasfff asdasdasasd'
listMsg = msg.split()
print listMsg,listMsg[0]


asd = search('ออม')
print asd,'123123'
