#!usr/bin/python3

import requests 

#call API and return day data and namesday
def namesday():

    call_api = requests.get("https://svatky.vanio.cz/api/")

    return call_api.text


print(namesday())

