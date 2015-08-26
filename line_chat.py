from line import LineClient, LineGroup, LineContact

USERNAME = 'yopachara@gmail.com'
PASSWORD = '024102124'
GROUPNAME = 'Evolution CS #13'
MSG = 'test'

#optional
COMPUTERNEME = 'yo'
#TOKEN = 'DV0yPSYwYQe1dLNZhJn1.oxhXCYbL5mot1nyKC+t0eq.w/+1EMvF/1L8/7Ht+UY852MvgUyv/xoZ0MvGLeg7+nI='
TOKEN = ''

try:
  client = LineClient(id=USERNAME, password=PASSWORD, authToken=TOKEN, com_name=COMPUTERNEME)
  #TOKEN = client.authToken
  print "TOKEN : %s\r\n" % TOKEN

  client_group = client.getGroupByName(GROUPNAME)
  recent_group_msg = client_group.getRecentMessages(count=10)
  print "RecentMessages : %s\r\n" % recent_group_msg

  client_group.sendMessage(MSG)

except:
    print "Login Failed"
