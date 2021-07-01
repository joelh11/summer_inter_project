#Write a python script that takes a sitemap XML file as an argument to the command line

import sys
import xmltodict
import requests

xml_sitemap = xmltodict.parse(requests.get('https://saberespoder.com/sitemap.xml').text)
xml_urls = [url["loc"] for url in xml_sitemap["urlset"]["url"]]

#print(len(xml_urls)) #there are 200 total urls, but i only need the articles
article_urls = xml_urls #new copy url set

i = 0
index = 0 #keeps track of the current index of the new url set
count = 0 #keeps track of how many article urls there are

#if 'https://saberespoder.com/articles/' in xml_urls[i]:
for i in range(len(xml_urls)): #do i not need to do length - 1? or is that just for c++
    if xml_urls[i].startswith('https://saberespoder.com/articles/'):
        article_urls[index] = xml_urls[i]
        index = index + 1
        count = count + 1

i = 0
for i in range(count): #prints all urls that are articles, while the rest after 'count' in the list are ignored
    print(article_urls[i])
#print("\n".join(xml_urls[0:200]))







