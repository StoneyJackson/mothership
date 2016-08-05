import glob
import makeHTML as html
import json
import base64

listt=glob.glob("./'IGh0d*'")

for index in listt:
    fileOpen = open('./'+index+'/meta.json', 'r')
    jsonFile = json.load(fileOpen)[base64.b64decode(index).decode('utf-8')]

    pageTitle = jsonFile['Data']['Title']
    print(pageTitle)
    pageHead = html.part('head')
    pageHead.addPart('title', pageTitle)
    pageBody = html.part('body')
    for item in jsonFile['Data']:
        pageBody.addPart('p', item + ': ' +str(jsonFile['Data'][item]))
        pageBody.addPart('br')
    fullPage = html.part('html')
    fullPage.addPiece(pageHead)
    fullPage.addPiece(pageBody)
    page = fullPage.make()
    fileOpen2 = open("./"+index+'/'+pageTitle+'.html','w')
    fileOpen2.write(page)
