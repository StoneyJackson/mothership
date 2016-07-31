import os
import json
import requests
import base64
from metadata_extractor_wip import main2
def createDir(url):
    encodedUrl = base64.b64encode(url.encode('ascii'))
    if checkDir(encodedUrl):
        encodedUrl = (str(encodedUrl).strip('b'))
    else:
        print('whoops')
    return encodedUrl

def checkDir(encodedUrl):
    #assume false
    statusOfDir = False

    if os.path.exists(encodedUrl) == False:
        statusOfDir = True #it exists


    return statusOfDir

def main():
    userNamePrompt = open('../config-location/config.txt', 'r').readline().strip('\n')#location of my
    promptForPassword = open('../config-location/oauth.txt', 'r').readline()#location of oauth file
    auth = (userNamePrompt, promptForPassword)
    openJson = open('urls.json', 'r')
    if os.stat('urls.json').st_size > 0:
        urlJson = json.load(openJson)
    urlList = urlJson['URLs']
    for url in urlList:
        try:
            direc = createDir(url)
            jsonFile = open('./'+direc+'./meta.json','r')
            etag = json.load(jsonFile)[url]['ETag']

            main2(url, auth, path=direc, etag = etag )
        except FileNotFoundError:
            os.mkdir(direc)
            main2(url, auth, path=direc)


main()
