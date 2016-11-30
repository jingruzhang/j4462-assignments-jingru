import json
import requests
import sys

url = "http://openstates.org/api/v1/legislators/?state=mo&active='true'"

url_1 = "http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&chamber=upper"

url_2 = "http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&chamber=upper&q=abortion"

url_3 = "http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&chamber=upper&q=education"

def active_mo_lawmakers():
    r = requests.get(url)

    response_data = r.text

    data = json.loads(response_data)

    for item in data:
        print item['first_name'],
        print item['last_name']
        print '=' * len(item['last_name'])

def newly_introduced_bills_mo_senate():
    r = requests.get(url_1)

    response_data = r.content

    data = json.loads(response_data)

    for item in data:
        print 'Bill title: "{}"'.format(item['title'])
        print 'Bill created at: {}'.format(item['created_at'])
        print 'Bill id: {}'.format(item['bill_id'])
        print "=" * len(item['bill_id'])
    print "There are {} bills introduced in 2016 in Missouri Senate.".format(len(data))

def abortion_bills_mo_senate_2016():
    r = requests.get(url_2)

    response_data = r.content

    data = json.loads(response_data)

    for item in data:
        print 'Bill title: "{}"'.format(item['title'])
        print 'Bill created at: {}'.format(item['created_at'])
        print 'Bill id: {}'.format(item['bill_id'])
        print "=" * len(item['bill_id'])
    print "There are {} abortion bills introduced in 2016 in Missouri Senate.".format(len(data))

def education_bills_mo_senate_2016():
    r = requests.get(url_3)

    response_data = r.content

    data = json.loads(response_data)

    for item in data:
    	bill_id = item['bill_id']
    	
    	detail_url = 'http://openstates.org/api/v1/bills/mo/2016/' + bill_id
    	
    	request = requests.get(detail_url)
    	
    	detail_data = json.loads(request.content)
    	
        print 'Bill title: "{}"'.format(item['title'])
        print 'Bill id: {}'.format(item['bill_id'])
        print 'Bill last action: {}'.format(detail_data["actions"][-1]["action"])
        print "=" * len(item['bill_id'])
    print "There are {} education bills introduced in 2016 in Missouri Senate.".format(len(data))

def show_help():
    print """Welcome to Open States api lookups.
    Type 1 to look up active lawmakers in Missouri. 
    Type 2 to look at all bills that've been introduced in 2016 Missouri Senate.
    Type 3 to look at all bills related to abortion introduced in 2016 Missouri Senate.
    Type 4 to look at all bills related to education introduced in 2016 Missouri Senate and the latest update of each bill.
    Type q to quit. """

show_help()

func_dict = {1: active_mo_lawmakers, 2: newly_introduced_bills_mo_senate, 3: abortion_bills_mo_senate_2016, 4: education_bills_mo_senate_2016}
task = raw_input('What do you want to do? 1/2/3/4/q. >')

if task != 'q':
    func_dict[int(task)]()
else:
    sys.exit()
