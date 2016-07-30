import os
import json
import requests
import base64


def createDir(url):
    encodedUrl = base64.b64encode(url.encode('ascii'))
    if checkDir(encodedUrl):
        print(encodedUrl)
        os.mkdir(encodedUrl)
    else:
        print('whoops')

def checkDir(encodedUrl):
    #assume false
    statusOfDir = False

    if os.path.exists(encodedUrl) == False:
        statusOfDir = True #it exists


    return statusOfDir

def main():
    openJson = open('urls.json', 'r')
    if os.stat('urls.json').st_size > 0:
        urlJson = json.load(openJson)
    urlList = urlJson['URLs']
    for url in urlList:
        createDir(url)




main()
