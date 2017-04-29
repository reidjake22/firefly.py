#! /usr/bin/env python

def get_tasks(user,password,auth, tasks):
    from cookielib import CookieJar
    from bs4 import BeautifulSoup
    from urllib import urlencode
    import urllib2
    import re
    FOUNDTASK = False
    AUTH_URL = tasks
    TASK_URL = auth
    TASKS = []
    DESCRIPTION = []
    FINALDICT = {}
    payload = {
      'Username': user,
      'Password': password
      }
    # Store the cookies and create an opener that will hold them
    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    # This is the target url
    data = urlencode(payload)
    # Makes a request (Data makes it a POST)
    req = urllib2.Request(AUTH_URL, data)
    resp = urllib2.urlopen(req)
    # With cookies it goes to the tasks URL to retrieve html
    response = urllib2.urlopen(TASK_URL)
    pageSource = response.read()
    # Parses html to get all <a> elements
    soup = BeautifulSoup(pageSource, "html.parser")  
    # Loop through all <a> elements
    for a in soup.find_all('a', href=True):
          # Checks for format set-tasks/123456 which all tasks have
          if re.findall(r'(set-tasks/\d{6}(?!\d))', a['href']):
               FOUNDTASK = True
               #Adds the <a> element to TASKS
               TASKS.append(a)
    #If there are any tasks
    if (FOUNDTASK):
        for tag in REFTASKS:
            # Add the text of each element to DESCRIPTION
            DESCRIPTION.append(str(tag.text))
        for i in range(0, len(REFTASKS)):
            # Form a dictionary of each task numbered as 1,2,3, ect ect  
            # with the six digit number in set-tasks/<6D> (as this can be used to access its description)
            #in an array with the description
            sigNum = REFTASKS[i]['href']
            sigNum = sigNum.encode('ascii', 'ignore')
            sigNum = sigNum.replace('set-tasks/', '')
            FINALDICT[i] = [sigNum,DESCRIPTION[i]]
    else:
        #if no tasks are found simply return one key and value of 0 and "NOT FOUND so checks can be made if so"
        FINALDICT[0] = "NOT FOUND"
    return FINALDICT