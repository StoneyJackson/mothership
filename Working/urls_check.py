import requests
import sys
userNamePrompt = open('../config-location/config.txt', 'r').readline().strip('\n')#location of my
yourPassWord = open('../config-location/oauth.txt', 'r').readline()#location of oauth file
#I wanted to the input url to be a ".git" url but I couldn't find any reference to that within the repos, interestingly
#enough its in the json returned from the GET request
inputUrl = str(input("Enter in the git URL to the git repo you'd like to retrieve metadata for: "))

partsOfUrl = inputUrl.split('/')
user = partsOfUrl[3]
repoName = partsOfUrl[4]
#URLS.md should in exist in the root
requestUrl = ("https://api.github.com/repos/%s/%s/contents/urls.md/" % (user, repoName))

request = requests.get(requestUrl, auth = (userNamePrompt, yourPassWord))
if request.status_code == 200: #successful request because file exists
    r2 = requests.get("https://raw.github.com/%s/%s/master/urls.md" % (user, repoName))
    urls = str(r2.content).strip('-').split(' ')
    urls = urls[1:]  #skip the first line its irrelevant and something github includes
    outJson = {}
    for url in urls:
        url = url.strip('\n')
        urlSplit = url.split('/')
        item = urlSplit[4].split('.')
        repo = item[0]
        outJson[repo] = url.split('\\')[0]
else:
    print("invalid url entered")
    sys.exit()

jsonFile = open('example.json','w')
jsonFile.write('[')
jsonFile.write('\n{\n')
for key in outJson:
    jsonFile.write('\t"' + key + '"' + " : " +  '"' + outJson[key] + '"' + ',\n' ) #need to modify so I don't have to write a comma on the last line as well
jsonFile.write('}')
jsonFile.write('\n]')
jsonFile.close()
print("Json file created successfully!")
#json = request.json()
#for key in json:
    #print(key,":",json[key])
