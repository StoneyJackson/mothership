import requests
inputUrl = str(input("Enter in the git URL to the git repo you'd like to retrieve metadata for: "))

partsOfUrl = inputUrl.split('/')
user = partsOfUrl[3]
repoName = partsOfUrl[4]

print(user, repoName)
requestUrl = ("https://api.github.com/repos/%s/%s" % (user, repoName))
request = requests.get(requestUrl, auth = ("tonytran", "***REMOVED***"))
print(request.status_code)
print(request.json())

json = request.json()
print(type(json))
for key in json:
    print(key,":",json[key])
