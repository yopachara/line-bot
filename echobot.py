#!/usr/bin/python
# -*- coding: UTF-8 -*-
from line import LineClient, LineGroup, LineContact
from searchJSON import search

#with open('/usr/local/lib/python2.7/site-packages/line/Persons.json') as data_file:
#    data = json.loads(data_file.read().decode('UTF-8'))
#output_file = codecs.open('/usr/local/lib/python2.7/site-packages/line/Persons.json','W',encoding='utf-8')

#search('Pachara')

USERNAME = ''
PASSWORD = ''
GROUPNAME = 'Evolution CS #13'
GROUPNAME1 = 'Test'
MSG = ''


#optional
COMPUTERNEME = 'bot yo'
#TOKEN = 'DV0yPSYwYQe1dLNZhJn1.oxhXCYbL5mot1nyKC+t0eq.w/+1EMvF/1L8/7Ht+UY852MvgUyv/xoZ0MvGLeg7+nI='
TOKEN = ''

try:
    client = LineClient(id=USERNAME, password=PASSWORD, authToken=TOKEN, com_name=COMPUTERNEME)
    group = client.getGroupByName(GROUPNAME1)
    print client.groups
    print TOKEN
    #client = LineClient(authToken='DV7I8leLWjKGX086Wtz1.oxhXCYbL5mot1nyKC+t0eq.ZMI9FeewbGOhkGJrj/8Adr4o0e+25v4bwf3opBJuhZU=')
except:
    print "Login Failed"
print 'Bot Ready !!!'

while True:
    op_list = []

    for op in client.longPoll():
        op_list.append(op)

    for op in op_list:
        sender   = op[0]
        receiver = op[1]
        message  = op[2]

        msg = message.text
        listMsg = msg.split()
        print listMsg
        if listMsg[0].lower() == 'find':
            try:
                result = search(listMsg[1])
                receiver.sendMessage("[%s]\n%s" % (sender.name, result))
                #receiver.sendMessage("[%s] %s" % (sender.name, 'โอ็ต เหม็นมากกกกก'))
            except:
                receiver.sendMessage("[%s]\n%s" % (sender.name, 'not found ja'))

#search('Pachara')
