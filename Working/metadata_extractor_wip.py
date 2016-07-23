import requests
import json
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

def getWatchers(user, repoName, auth):
    watchUrl = ("https://api.github.com/repos/%s/%s/subscribers"% (user,repoName))
    numPages = getNumPages(watchUrl, auth)
    link = watchUrl
    i = 1
    runtime = 0
    total = 0
    names = []
    if numPages == 0: #do a non paginated request
        watchUrl =  "https://api.github.com/repos/%s/%s/subscribers"% (user,repoName)
        watchersRequest = requests.get(watchUrl, auth = auth)
        watchers = watchersRequest.json()
        for name in watchers:
            if name['login'] not in names:
                names+=[name['login']]
    else:
        for page in range(numPages+1):
            watchUrl =  "https://api.github.com/repos/%s/%s/subscribers?page=%i"% (user,repoName,page)
            watchersRequest = requests.get(watchUrl, auth = auth)
            watchers = watchersRequest.json()
            for name in watchers:
                if name['login'] not in names:
                    names+=[name['login']]

    return len(names)


def getCommits(user, repoName, auth):
    commUrl = ("https://api.github.com/repos/%s/%s/commits"% (user,repoName))
    numPages = getNumPages(commUrl, auth)
    commitsList = []
    print(len(commitsList))
    if numPages == 0: #do a non paginated request
        commUrl =  "https://api.github.com/repos/%s/%s/commits"% (user,repoName)
        commitsRequest = requests.get(commUrl, auth = auth)
        commits = commitsRequest.json()
        for commit in commits:
            commitsList+=[commit]
    else:
        for page in range(numPages+1):
            watchUrl =  "https://api.github.com/repos/%s/%s/commits?page=%i"% (user,repoName,page)
            commitsRequest = requests.get(commUrl, auth = auth)
            commits = commitsRequest.json()
            for commit in commits:
                commitsList+=[commit]


    return len(commitsList)

#need to use a different URL
def getContributors(user, repoName, auth):
    watchUrl = ("https://api.github.com/repos/%s/%s/contributors"% (user,repoName))
    numPages = getNumPages(watchUrl, auth)
    link = watchUrl
    names = []
    if numPages == 0: #do a non paginated request
        watchUrl =  "https://api.github.com/repos/%s/%s/contributors"% (user,repoName)
        watchersRequest = requests.get(watchUrl, auth = auth)
        watchers = watchersRequest.json()
        for name in watchers:
            if name['login'] not in names:
                names+=[name['login']]
    else:
        for page in range(numPages+1):
            watchUrl =  "https://api.github.com/repos/%s/%s/contributors?page=%i"% (user,repoName,page)
            watchersRequest = requests.get(watchUrl, auth = auth)
            watchers = watchersRequest.json()
            for name in watchers:
                if name['login'] not in names:
                    names+=[name['login']]

    return len(names)
def getMetadata(user, repoName, auth):
    #this will get the title, description, watchers, stars, subscribers?, forks
    metadataUrl = ("https://api.github.com/repos/%s/%s" % (user, repoName))
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


def writeJson(metaDict):
    jsonFile = open('meta.json', 'w')
    json_data = json.dumps(metaDict)
    jsonFile.write(json_data)
    jsonFile.close()
    print("Json file created successfully!")
def main():
    #userNamePrompt = str(input("Enter in your github username: "))
    #chooseMethod = int(input("Enter in 1 for authentication through OAuth, 2 for Username + Password: "))
    chooseMethod = 1
    userNamePrompt = open('../config-location/config.txt', 'r').readline().strip('\n')#location of my
    promptForPassword = open('../config-location/oauth.txt', 'r').readline()#location of oauth file
    auth = (userNamePrompt, promptForPassword)
    inputUrl = str(input("Enter in the git URL to the git repo you'd like to retrieve metadata for: "))
    partsOfUrl = inputUrl.split('/')
    user = partsOfUrl[3]
    repoName = partsOfUrl[4]
    numWatchers = getWatchers(user, repoName, auth)
    numContributors = getContributors(user, repoName, auth)
    metadataDict, etag = getMetadata(user,repoName,auth)
    lastCommitDict = getLastCommit(user, repoName, auth)
    numCommits = getCommits(user, repoName, auth)
    repoDict = parseDict(inputUrl, metadataDict, numContributors, numCommits, lastCommitDict, numWatchers, etag)
    writeJson(repoDict)



main()
