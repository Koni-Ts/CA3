from requests import get, post
import json
from dateutil import parser
import datetime
import os
import requests
import bs4
from bs4 import BeautifulSoup
import re

# Module variables to connect to moodle api:
## Insert token and URL for your site here. 
## Mind that the endpoint can start with "/moodle" depending on your installation.
KEY = "8cc87cf406775101c2df87b07b3a170d" 
URL = "https://034f8a1dcb5c.eu.ngrok.io"
ENDPOINT="/webservice/rest/server.php"

def rest_api_parameters(in_args, prefix='', out_dict=None):
    """Transform dictionary/array structure to a flat dictionary, with key names
    defining the structure.
    Example usage:
    >>> rest_api_parameters({'courses':[{'id':1,'name': 'course1'}]})
    {'courses[0][id]':1,
     'courses[0][name]':'course1'}
    """
    if out_dict==None:
        out_dict = {}
    if not type(in_args) in (list,dict):
        out_dict[prefix] = in_args
        return out_dict
    if prefix == '':
        prefix = prefix + '{0}'
    else:
        prefix = prefix + '[{0}]'
    if type(in_args)==list:
        for idx, item in enumerate(in_args):
            rest_api_parameters(item, prefix.format(idx), out_dict)
    elif type(in_args)==dict:
        for key, item in in_args.items():
            rest_api_parameters(item, prefix.format(key), out_dict)
    return out_dict

def call(fname, **kwargs):
    """Calls moodle API function with function name fname and keyword arguments.
    Example:
    >>> call_mdl_function('core_course_update_courses',
                           courses = [{'id': 1, 'fullname': 'My favorite course'}])
    """
    parameters = rest_api_parameters(kwargs)
    parameters.update({"wstoken": KEY, 'moodlewsrestformat': 'json', "wsfunction": fname})
    #print(parameters)
    response = post(URL+ENDPOINT, data=parameters).json()
    if type(response) == dict and response.get('exception'):
        raise SystemError("Error calling Moodle API\n", response)
    return response

################################################
# Rest-Api classes
################################################

class LocalGetSections(object):
    """Get settings of sections. Requires courseid. Optional you can specify sections via number or id."""
    def __init__(self, cid, secnums = [], secids = []):
        self.getsections = call('local_wsmanagesections_get_sections', courseid = cid, sectionnumbers = secnums, sectionids = secids)

################################################
# Example
################################################

courseid = "18" # Exchange with valid id.

# # Get all sections of the course.
sec = LocalGetSections(courseid)
# print(sec.getsections)

# print(json.dumps(sec.getsections, indent=4, sort_keys=True ))

# print(json.dumps(sec.getsections[0] ['summary'], indent=4, sort_keys=True ))

# print(json.dumps(sec.getsections[1] ['summary'], indent=4, sort_keys=True ))



# #Function to read through the directory and give a dictionary of files per folder
def folders(path):
    y=list()
    for f in sorted(os.listdir(path)):
        if not f.endswith(".py") and not f.endswith(".git"):
            y.append(f)
    print(y)

def html_files(direct):
    x = [i[2] for i in sorted(os.walk(direct))]
    y=list()
    for t in x:
        for f in t:
            if f.endswith(".html"):
                y.append(f)
            
    print(y)

def md_files(direct):
    x = [i[2] for i in sorted(os.walk(direct))]
    y=list()
    for t in x:
        for f in t:
            if f.endswith(".md"):
                y.append(f)
    print(y)

def pdf_files(direct):
    x = [i[2] for i in sorted(os.walk(direct))]
    y=list()
    for t in x:
        for f in t:
            if f.endswith(".pdf"):
                y.append(f)
    print(y)

h=folders('/workspace/CA3')
i=html_files('/workspace/CA3')
j=md_files('/workspace/CA3')
k=pdf_files('/workspace/CA3')

#combine the lists into a dictionary
combine_list=dict(zip(h,i,j,k))




# #attempt to update sections where the values are empty " " (intetion to use items from the above list)
# d=json.dumps(sec.getsections, indent=4, sort_keys=True )
# for x in d:
#     x.update((k, "value3") for k, v in d.items() if v == " ")
# print(d)



# A class to update objects in the actual moodle page (code given in class)
class LocalUpdateSections(object):
    """Updates sectionnames. Requires: courseid and an array with sectionnumbers and sectionnames"""

    def __init__(self, cid, sectionsdata):
        self.updatesections = call(
            'local_wsmanagesections_update_sections', courseid=cid, sections=sectionsdata)

courseid = "18"
sec = LocalGetSections(courseid)
data = [{'type': 'num', 'section': 0, 'summary': '', 'summaryformat': 1, 'visible': 1 , 'highlight': 0, 'sectionformatoptions': [{'name': 'level', 'value': '1'}]}]
# Assemble the correct summary
summary = '<a href="https://mikhail-cct.github.io/ca3-test/wk1/">Week 1: Introduction</a><br>'

# Assign the correct summary
data[0]['summary'] = summary

# Set the correct section number
data[0]['section'] = 8

# Write the data back to Moodle
sec_write = LocalUpdateSections(courseid, data)




#screaping the google drive with BeautifulSoup to get the links and titles of video
URL = 'https://drive.google.com/drive/folders/1pFHUrmpLv9gEJsvJYKxMdISuQuQsd_qX'
page = requests.get(URL)


soup = bs4.BeautifulSoup(page.text,"lxml")  
hash_vid = soup.find_all('div',class_ = 'Q5txwe')

#create 2 lists one with hash ids and one for the titles of the video
video_id=[]
titles=[]
#iterate through the soup to get the list values
for video in hash_vid:
    # print(video)
	video_id.append(video.parent.parent.parent.parent.attrs['data-id'])
	titles.append(video.text)
print(video_id)
print(titles)


#function prepend the url before the video hash ID
def prepend(list, str): 
      
    # Using format() 
    str += '{0}'
    list = [str.format(i) for i in list] 
    return(list) 


link_prefix= "https://drive.google.com/file/d/"
full_link=prepend(video_id, link_prefix)
print(prepend(video_id, link_prefix))


#create a dictionary with the title of the video and url
link_and_title=dict(zip(titles, full_link))

print(link_and_title)