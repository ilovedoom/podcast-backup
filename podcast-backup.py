# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:42:04 2021

@author: ilovedoom - thePixelsChips
"""


import requests
import xml.etree.ElementTree as ET

print("welcome to the podcast downloader")
originalurl = input("paste the URL of feed RSS of the podcast and press Enter. ")
podcastname = input("name of the podcast.. ")
r = requests.get(originalurl, allow_redirects=True)
xmlrss = 'rss'+podcastname+'.xml'
print(xmlrss)

open(xmlrss, 'wb').write(r.content)

episodes = ET.parse(xmlrss)
url2download = 'none'
episodeTitle = 'none'
filename = 'none'
filetype = 'none'
fileextension = 'none'


for elem in episodes.iter():


    if elem.tag =='title':

        episodeTitleRaw = elem.text
        episodeTitle = episodeTitleRaw.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        print(episodeTitle)
        

    if elem.tag =='enclosure':

        enclosureJson = elem.attrib
        url2download = str(enclosureJson["url"])

        print(url2download)
        filetype = str(enclosureJson["type"])
        print(filetype)
        if filetype == 'audio/x-m4a':
            fileextension = '.m4a'
            print(fileextension)
            filename = episodeTitle + fileextension
            print(filename)
            r = requests.get(url2download, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            print("ended download")
        else:
            fileextension = '.mp3'
            print(fileextension)
            filename = episodeTitle + fileextension
            print(filename)
            r = requests.get(url2download, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            print("ended download")

print("ended. thanks.")
