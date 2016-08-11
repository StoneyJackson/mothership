import os
import json
import requests
import base64

from metadata_extractor_wip import main2
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('type', help = 'type OAuth to use OAuth authentication (ensure you have an OAuth.txt file in your config folder first)', nargs='?', const='Standard')
args = parser.parse_args()

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

    if args.type == 'OAuth':
        yourPassWord = open('../config-location/oauth.txt', 'r').readline()#location of oauth file
    else:
        yourPassWordFile = open('../config-location/config.txt', 'r')
        yourPassWordFile.readline()
        promptForPassword = yourPassWordFile.readline().strip('\n')
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
