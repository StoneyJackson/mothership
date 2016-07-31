import requests
import json
import sys
#need to use a different URL
def getNumPages(url, auth):

    link = url
    request = requests.get(link, auth = auth)

    try:
        lastPage = request.headers['Link'].split(';')[1].split('?')[1].split('=')[1]
        numPages = int(lastPage.strip('>'))
    except KeyError:  #some of these requests wont have pagination because they're only one page
        numPages = 0
    return numPages

#need to use a different URL
def getData(user, repoName, auth, dataType):
    requestUrl = ("https://api.github.com/repos/"+user+"/"+repoName+"/"+dataType)
    numPages = getNumPages(requestUrl, auth)
    dataList = []
    if numPages == 0: #do a non paginated request
        requestUrl =  "https://api.github.com/repos/"+user+"/"+repoName+"/"+dataType
        dataRequest = requests.get(requestUrl, auth = auth)
        dataJson = dataRequest.json()
        for data in dataJson:
            if dataType != 'commits':
                if data['login'] not in dataList: #contributors and watchers have this
                    dataList+=[data['login']]
            else:
                dataList += [data]
    else:
        for page in range(numPages+1):
            watchUrl =  "https://api.github.com/repos/"+user+"/"+repoName+"/"+dataType+"?page="+ str(page)
            dataRequest = requests.get(requestUrl, auth = auth)
            dataJson = dataRequest.json()
            for data in dataJson:
                if dataType != 'commits':
                    if data['login'] not in dataList:
                        dataList+=[data['login']]
                else:
                    dataList += [data]

    return len(dataList)
def getMetadata(user, repoName, auth, **kwargs):
    #this will get the title, description, watchers, stars, subscribers?, forks
    metadataUrl = ("https://api.github.com/repos/%s/%s" % (user, repoName))
    if 'checkstat' in kwargs:
        etagToCheck = kwargs['checkstat']
        if etagToCheck == requests.get(metadataUrl, auth = auth).headers['etag'].strip('\"'):
            print('ETag is the same no updating necessary')
            sys.exit()
        else: #etag is not the same so update
            metadataRequest = requests.get(metadataUrl, auth = auth)
            metadataJson = metadataRequest.json()
            title = metadataJson["name"]
            description = metadataJson["description"]
            stars = metadataJson["stargazers_count"]
            forks = metadataJson["forks_count"]
            metaEtag = metadataRequest.headers['etag'].strip('\"')
            metadata = {}

            metadata["Title"] = title
            metadata["Repo Description"] = description
            metadata["Stars"] = stars
            metadata["Number of forks"] = forks
            return metadata, metaEtag
    else: #no etag to pass since it doesn't exist
        metadataRequest = requests.get(metadataUrl, auth = auth)
        metadataJson = metadataRequest.json()
        title = metadataJson["name"]
        description = metadataJson["description"]
        stars = metadataJson["stargazers_count"]
        forks = metadataJson["forks_count"]
        metaEtag = metadataRequest.headers['etag'].strip('\"')
        metadata = {}

        metadata["Title"] = title
        metadata["Repo Description"] = description
        metadata["Stars"] = stars
        metadata["Number of forks"] = forks
        return metadata, metaEtag
def getLastCommit(user, repo, auth):
    url = 'https://api.github.com/repos/%s/%s/git/refs/heads/master' % (user, repo)
    master = requests.get(url, auth = auth)
    commitObjUrl = master.json()['object']['url']
    lastComm = requests.get(commitObjUrl, auth = auth)
    lastcommit =  lastComm.json()
    lastCommitDict = {}
    lastCommitDict['Author'] = lastcommit['author']['name']
    lastCommitDict['Message'] = lastcommit['message']
    return lastCommitDict
def parseDict(repoUrl,metadataDict, contributorsNum, commitsNum, lastCommitDict, watchersnum, etag):
    repoDict = {}
    repoDict['ETag'] = etag
    metaDict = {}
    metadataDict['Contributors'] = contributorsNum
    metadataDict['Commits'] = commitsNum
    metadataDict['Watchers'] = watchersnum
    repoDict['Data'] = metadataDict
    repoDict['Last Commit'] = lastCommitDict
    metaDict[repoUrl] = repoDict
    return metaDict


def writeJson(metaDict, **kwargs):
    if ('path' in kwargs):
        print('path specified')
        path = kwargs['path']
        jsonFile = open('./'+str(path)+'/meta.json', 'w')
    else:
        print('no path specified')
        jsonFile = open('meta.json', 'w')
    json_data = json.dumps(metaDict)
    jsonFile.write(json_data)
    jsonFile.close()
    print("Json file created successfully!")

def main2(inputUrl, auth, **kwargs):
    partsOfUrl = inputUrl.split('/')
    user = partsOfUrl[3]
    repoName = partsOfUrl[4].split('.')[0]
    if 'etag' in kwargs:
        etagToCheck = kwargs['etag']
        metadataDict, etag = getMetadata(user,repoName,auth, checkstat = etagToCheck)
    else:
        metadataDict, etag = getMetadata(user,repoName,auth )

        numWatchers = getData(user, repoName, auth, 'subscribers')
        numContributors = getData(user, repoName, auth, 'contributors')

    if metadataDict is None:
        print('ETag is the same no updating necessary')
        sys.exit()
    lastCommitDict = getLastCommit(user, repoName, auth)
    numCommits = getData(user, repoName, auth, 'commits')
    repoDict = parseDict(inputUrl, metadataDict, numContributors, numCommits, lastCommitDict, numWatchers, etag)
    if 'path' in kwargs:
        writeJson(repoDict, path = kwargs['path'])
    else:
        writeJson(repoDict)
def main():
    #userNamePrompt = str(input("Enter in your github username: "))
    #chooseMethod = int(input("Enter in 1 for authentication through OAuth, 2 for Username + Password: "))
    chooseMethod = 1
    userNamePrompt = open('../config-location/config.txt', 'r').readline().strip('\n')#location of my
    promptForPassword = open('../config-location/oauth.txt', 'r').readline()#location of oauth file
    auth = (userNamePrompt, promptForPassword)
    inputUrl = str(input("Enter in the git URL to the git repo you'd like to retrieve metadata for: "))
    main2(inputUrl, auth)


if __name__ == "__main__":
    main()
