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

it requires a url to be passed, repo must contain urls.md *
also takes an optional 'OAuth' argument to choose to use an OAuth file to authenticate
(note if you've set up MFA on your github, I recommend setting up OAuth) 
I ran this with https://github.com/foss2serve/corral


2. run harvester.py
this will also require a url argument
and OAuth or standard authentication are avialable options
it will generate a folder for each url in urls.md and each folder will contain a meta.json

3. run generateHTML.py - for now it will generate very basic html no css(To be added later)
#Example
If you didn't have MFA set up, you would run it like so.
```
location/to/repo> python urls_check.py https://github.com/foss2serve/corral
location/to/repo> python harvester.py
location/to/repo> python generateHTML.py
```
If you did have MFA set up like I do, you'll need to use OAuth like so.
```
location/to/repo> python urls_check.py https://github.com/foss2serve/corral OAuth **
location/to/repo> python harvester.py OAuth
location/to/repo> python generateHTML.py
```
*Note: If the repository entered doesn't contain a URLS.md on the root, it will return an HTTP 404 error.
**Note: If you don't add OAuth, you will get an HTTP 401 error, and the program will exit.


4. (Optional) You can edit the css for the html pages by navigating into harvester/css/ref.css

## Copyright and License

* Copyright 2016, Stoney Jackson SOME RIGHTS RESERVED
* License: GPLv3
