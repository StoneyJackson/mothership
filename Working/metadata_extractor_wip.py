import requests

#need to use a different URL

def getWatchers(user, repoName, auth):
    watchUrl = ("https://api.github.com/repos/%s/%s/subscribers"% (user,repoName))
    link = watchUrl
    i = 1
    runtime = 0
    total = 0
    names = []
    while runtime != 35:
        watchRequest = requests.get(link, auth = auth)
        watchJson = watchRequest.json()
        print(len(watchJson))
        for item in watchJson:
            total+=1
            name = (item["login"])
            print(name)
            names += [name]

        link = ("https://api.github.com/repositories/3620194/subscribers?page=%i" % (runtime))
        #print("Next link: ", i)
        i+=1
        runtime+=1
    print("Number of subscribers: ", total)
    print("Number: ", len(names))


def getCommits(user, repoName, auth):
    '''link = "something"
    commits2 = ("https://api.github.com/repos/%s/%s/commits" % (user, repoName))
    comm2 = requests.get(commits2, auth = auth)
    comm2json = comm2.json()'''
    pass
    #commitsUrl = ("https://api.github.com/repos/%s/%s/contributors" % (user, repoName))

#need to use a different URL
def getContributors(user, repoName, auth):
    commitsUrl = ("https://api.github.com/repos/%s/%s/contributors" % (user, repoName))
    commitsRequest = requests.get(commitsUrl, auth = auth)
    commJson = commitsRequest.json()
    commits = 0
    contributorNum = 0
    for val in commJson:
        contributor = commJson[contributorNum]
        commits+=contributor["contributions"]
        contributorNum += 1
    print("Number of contributors: ",contributorNum)
def getMetadata(user, repoName, auth):
    #this will get the title, description, watchers, stars, subscribers?, forks
    metadataUrl = ("https://api.github.com/repos/%s/%s" % (user, repoName))
    metadataRequest = requests.get(metadataUrl, auth = auth)
    metadataJson = metadataRequest.json()
    title = metadataJson["name"]
    description = metadataJson["description"]
    stars = metadataJson["stargazers_count"]
    forks = metadataJson["forks_count"]
    print("Title: ", title)
    print("Repo Description: ", description)
    print("Stars: ",stars)
    print("Number of forks: ", forks)
def getLastCommit():
    pass
def main():
    #userNamePrompt = str(input("Enter in your github username: "))
    #chooseMethod = int(input("Enter in 1 for authentication through OAuth, 2 for Username + Password: "))
    userNamePrompt =  "tonytran"
    chooseMethod = 1
    promptforOauth = "C:\\Users\\tonyb\\Desktop\\google app\\oauth.txt"
    if (chooseMethod == 1):
        #promptforOauth = str(input("Enter in the location of your OAuth token "))
        authFile =  open(promptforOauth)
        authLine = authFile.readline()
        authFile.close()
        print(authLine)
        auth = (userNamePrompt, authLine)

    else: #its 2
        promptForPassword = str(input("Enter in the password for your github: "))
        auth = (userNamePrompt, promptForPassword)
    inputUrl = str(input("Enter in the git URL to the git repo you'd like to retrieve metadata for: "))
    partsOfUrl = inputUrl.split('/')
    user = partsOfUrl[3]
    repoName = partsOfUrl[4]
    getWatchers(user, repoName, auth)
    getContributors(user, repoName, auth)
    getMetadata(user,repoName,auth)




main()
