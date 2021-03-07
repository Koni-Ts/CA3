import requests
import bs4
from bs4 import BeautifulSoup
import re

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

