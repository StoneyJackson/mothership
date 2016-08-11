#Harvester use Documentation


by Tony Tran

##About Harvester
Harvester is a proof of concept project that visits Github repositories, grabs the metadata and generates a webpage for each repo.
##Dependencies
To use the harvester you need: Python 3.x,
and A github account

In addition you'll also need the requests module found [here] (http://docs.python-requests.org/en/master/)
and the makeHTML module which can be found [here](http://www.hoboes.com/Mimsy/hacks/object-oriented-html/)

##Setup
1. To use the harvester you must have a github account to authenticate
2. Harvester supports authentication by OAuth or a standard username and password
3. With that in mind, you should have a folder named config-location located on the root of the repo.
4. Your config-location should have a config.py that contains your authentication information
as well as an OAuth text file that holds your OAuth token.
config.py
```
DATA_ROOT = 'path/to/where/we/should/store/data'
GITHUB_ROOT = 'https://api.github.com'
GITHUB_USERNAME = 'Your Username'
GITHUB_PASSWORD = 'Your Password'

```

##Usage
1. run urls_check.py


it requires a url to be passed, repo must contain urls.md
also takes an optional 'OAuth' argument to choose to use an OAuth file to authenticate
(note if you've set up MFA on your github, I recommend setting up OAuth) 
I ran this with https://github.com/foss2serve/corral


2. run harvester.py
this will also require a url argument
and OAuth or standard authentication are avialable options
it will generate a folder for each url in urls.md and each folder will contain a meta.json

3. run generateHTML.py - for now it will generate very basic html no css(To be added later)



