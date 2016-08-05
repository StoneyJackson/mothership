#Harvester use Documentation


by Tony Tran


1. To use the harvester you must have a github account to authenticate
2. Harvester supports authentication by OAuth or a standard username and password
3. With that in mind, you should have a folder named config-location located on the root of the repo.
4. Your config-location should have a config.py that contains your authentication information
as well as an OAuth text file that holds your OAuth token.

Now to run the harvester you'll need the following dependencies

os,json,base64,requests,sys,glob, and makeHTML
which can be found [here](http://www.hoboes.com/Mimsy/hacks/object-oriented-html/):

these should all be available natively, harvester was built on Python 3.x
so I would recommend having that version.

5. run urls_check.py

it will prompt for a url, this url should point to a repo containing a urls.md file
I ran this with https://github.com/foss2serve/corral

6. run harvester.py
it will generate a folder for each url in urls.md and each folder will contain a meta.json
7. run generateHTML.py - for now it will generate very basic html no css(To be added later)
