import urllib2
import json
import datetime
import csv
import time
import pprint




def request_until_succeed(url):
    req = urllib2.Request(url)
    success = False
    while success is False:
        try: 
            response = urllib2.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception, e:
            print e
            time.sleep(5)
            
            print "Error for URL %s: %s" % (url, datetime.datetime.now())

    return response.read()
    


def getFacebookPageFeedData(page_id, access_token, num_statuses):
    
    # construct the URL string
    base = "https://graph.facebook.com"
    node = "/" + page_id + "/feed" 
    parameters = "/?fields=message,link,created_time,type,name,id,shares&limit=%s&access_token=%s" % (int(num_statuses), str(access_token)) # changed
    url = base + node + parameters
    
    
    
    data=request_until_succeed(url)
    #print data
    #pprint.pprint(data, width=1)
    data = json.loads(data)
    #print data
    return data
    
def unicode_normalize(text):
	return text.translate({ 0x2018:0x27, 0x2019:0x27, 0x201C:0x22, 0x201D:0x22, 0xa0:0x20 }).encode('utf-8')


#print json.dumps(test_status, indent=4, sort_keys=True)



def processFacebookPageFeedStatus(status):
    
    
    status_id = status['id']
    status_message = '' if 'message' not in status.keys() else unicode_normalize(status['message'])
    link_name = '' if 'name' not in status.keys() else unicode_normalize(status['name'])
    status_type = status['type']
    status_link = '' if 'link' not in status.keys() else unicode_normalize(status['link'])
    
    
    # Time needs special care since a) it's in UTC and
    # b) it's not easy to use in statistical programs.
    
    status_published = datetime.datetime.strptime(status['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
    status_published = status_published + datetime.timedelta(hours=-5) # EST
    status_published = status_published.strftime('%Y-%m-%d %H:%M:%S') # best time format for spreadsheet programs
    
    # Nested items require chaining dictionary keys.
    
    num_reactions = 0 if 'reactions' not in status.keys() else status['reactions']['summary']['total_count']
    num_comments = 0 if 'comments' not in status.keys() else status['comments']['summary']['total_count']
    num_shares = 0 if 'shares' not in status.keys() else status['shares']['count']
    
    # return a tuple of all processed data
    return (status_id, status_message, link_name, status_type, status_link,
           status_published, num_reactions, num_comments, num_shares)


def stingwithnextline(x):
    if len(x)>3:
    	return x+"\n"
    else:
    	return ""

def main(text):
    app_id = ""
    app_secret = "" 

    access_token = app_id + "|" + app_secret

    page_id = str(text)
    #testFacebookPageFeedData(page_id, access_token)
    test_status = getFacebookPageFeedData(page_id, access_token,'10')["data"]
    #print test_status
    x=""
    i=0
    while i<10:
    	data=test_status[i]
    	processed_test_status = processFacebookPageFeedStatus(data)
    	y =processed_test_status[1].splitlines()
    	z=""
    	for a in y:
    		if len(a)>3:
    			z=z+a
    			
    	#if processed_test_status[3]=="photo" or processed_test_status[3]=="video":
    	fdata=str(stingwithnextline(z))+str(stingwithnextline(processed_test_status[2]))+str(stingwithnextline(processed_test_status[4]))+str(stingwithnextline(processed_test_status[5]))
    	
    	
    	
    	'''
    	if len(processed_test_status[0])<3:
    	    fdata="title : video"+"\nLink : "+str(processed_test_status[1])+'\nDetails : '+str(processed_test_status[2])  
    	else:
    	    fdata="title : "+str(processed_test_status[0])+"\nLink : "+str(processed_test_status[1])+'\nDetails : '+str(processed_test_status[2])+"\n new"+str(processed_test_status[3])+"\n new"+str(processed_test_status[4])+"\n new"+str(processed_test_status[5])+"\n new"+str(processed_test_status[6])+"\n new"+str(processed_test_status[7])+"\n new"+str(processed_test_status[8])
    	'''
    	x=x+"\n\n\n"+fdata
    	i=i+1
    return x
    #print "--------------------------------"
    
    #processed_test_status = processFacebookPageFeedStatus(test_status)
    #print processed_test_status
    #return processed_test_status
    #scrapeFacebookPageFeedStatus(page_id, access_token)
    '''
while 1:
	main(str(raw_input()))
    '''
