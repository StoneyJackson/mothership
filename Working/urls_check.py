import requests
import sys
import json
import os



def getUrls(requestUrl, user, repoName, auth, urlsJson):
    urlList = []
    repoList = []

    request = requests.get(requestUrl, auth = auth)

    if request.status_code == 200: #successful request because file exists
        r2 = requests.get("https://raw.github.com/%s/%s/master/urls.md" % (user, repoName))
        if r2.status_code == 200:
            if os.stat('urls.json').st_size > 0:
                if urlsJson['ETag'] != None: #no etag? if possible need to check
                    if urlsJson['ETag'] != r2.headers['ETag'].strip('\"'):
                        etag = (r2.headers['ETag'].strip('\"'))
                        urls = str(r2.content).strip('-').split(' ')
                        urls = urls[1:]  #skip the first line its irrelevant and something github includes
                        for url in urls:
                            url = url.strip('\n')
                            url = url.rstrip().rstrip()

                            urlList += [url]
                            urlSplit = url.split('/')
                            item = urlSplit[4].split('.')
                            repo = item[0]
                            repoList += [repo]

                    else:
                        print('Request has the same ETag exiting since no changes have been made.')
                        sys.exit()
            else:
                etag = (r2.headers['ETag'].strip('\"'))
                urls = str(r2.content).strip('-').split(' ')
                urls = urls[1:]  #skip the first line its irrelevant and something github includes
                for url in urls:
                    url = url.strip('\n')
                    url = url.rstrip().rstrip()

                    urlList += [url]
                    urlSplit = url.split('/')
                    item = urlSplit[4].split('.')
                    repo = item[0]
                    repoList += [repo]
                else: #urls.md does not exist so create it?
                    createMD = open('urls.md', 'w')
                    createMD.close()
    else:
        print("invalid url entered")
        sys.exit()

    return urlList, repoList, etag
def parseDict(urlList, repoList, etag):
    urlsDict = {}
    urlsDict['ETag'] =  etag
    print(etag)
    print(urlsDict['ETag'])
    urlsDict['URLs'] = urlList
    #for repo in repoList:
        #repoDict[repo] = urlList[repoList.index(repo)]
    return urlsDict
def writeJson(repoDict, json_fileName):
    jsonFile = open('urls.json','w')
    json_data = json.dumps(repoDict)
    jsonFile.write(json_data)
    jsonFile.close()
    print("Json file created successfully!")

def main():
    try:
        openJson = open('urls.json', 'r')
        if os.stat('urls.json').st_size > 0:
            urlJson = json.load(openJson)
    except FileNotFoundError:
        urlJson = open('urls.json', 'w')
    userNamePrompt = open('../config-location/config.txt', 'r').readline().strip('\n')#location of my
    yourPassWord = open('../config-location/oauth.txt', 'r').readline()#location of oauth file
    #I wanted to the input url to be a ".git" url but I couldn't find any reference to that within the repos, interestingly
    #enough its in the json returned from the GET request
    inputUrl = str(input("Enter in the git URL to the git repo you'd like to retrieve metadata for: "))
    auth = (userNamePrompt, yourPassWord)
    partsOfUrl = inputUrl.split('/')
    user = partsOfUrl[3]
    repoName = partsOfUrl[4]
    #URLS.md should in exist in the root
    requestUrl = ("https://api.github.com/repos/%s/%s/contents/urls.md/" % (user, repoName))
    urlList, repoList, etag = getUrls(requestUrl, user, repoName, auth, urlJson)
    urlsDict = parseDict(urlList, repoList, etag)
    writeJson(urlsDict, 'urls')

main()

#json = request.json()
#for key in json:
    #print(key,":",json[key])
