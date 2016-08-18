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

### 1. Create and edit config file

Place config file in PROJECT_ROOT/config-location/config.py . Paste the following into that file and edit to your liking.

```
DATA_ROOT = 'path/to/where/we/should/store/data'
GITHUB_ROOT = 'https://api.github.com'
GITHUB_USERNAME = 'Your Username'
GITHUB_PASSWORD = 'Your Password'
```

### 2. (Optional) OAuth

If you are going to use OAuth, put your OAuth key in a plain text file. This documenation assumes you put it in a file named oauth.txt and it is in the root of this program.


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



