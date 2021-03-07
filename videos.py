import requests
import bs4
from bs4 import BeautifulSoup
import re

URL = 'https://drive.google.com/drive/folders/1pFHUrmpLv9gEJsvJYKxMdISuQuQsd_qX'
page = requests.get(URL)


soup = bs4.BeautifulSoup(page.text,"lxml")  
hash_vid = soup.find_all('div',class_ = 'Q5txwe')


video_id=[]
for video in hash_vid:
    # print(video)
	video_id.append(video.parent.parent.parent.parent.attrs['data-id'])
	title = video.text

print(video_id)

def prepend(list, str): 
      
    # Using format() 
    str += '{0}'
    list = [str.format(i) for i in list] 
    return(list) 

link_prefix= "https://drive.google.com/file/d/"

print(prepend(video_id, link_prefix))




