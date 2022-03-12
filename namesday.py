#!/usr/bin/python3

from unicodedata import name
import requests 
import re

#call API and return day data and namesday
def namesday():

    call_api = requests.get("https://svatky.vanio.cz/api/")

    return call_api.text

print(namesday())



def find_name():
    
    find = re.findall('name:([\s\S]*)$', namesday())

    find_string = ' '.join(find)

    return find_string

print(find_name())