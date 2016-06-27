import requests
userNamePrompt = str(input("Enter in your github username: "))
yourPassWord = str(input("Enter in your github password: "))
#I wanted to the input url to be a ".git" url but I couldn't find any reference to that within the repos, interestingly 
#enough its in the json returned from the GET request
inputUrl = str(input("Enter in the git URL to the git repo you'd like to retrieve metadata for: "))

partsOfUrl = inputUrl.split('/')
user = partsOfUrl[3]
repoName = partsOfUrl[4]

requestUrl = ("https://api.github.com/repos/%s/%s" % (user, repoName))
request = requests.get(requestUrl, auth = (yourUserName, yourPassWord))


json = request.json()
for key in json:
    print(key,":",json[key])
