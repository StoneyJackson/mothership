import glob
import makeHTML as html
import json
import base64

listt=glob.glob("./'IGh0d*'")

for index in listt:
    file_open = open('./'+index+'/meta.json', 'r')
    json_file = json.load(file_open)[base64.b64decode(index).decode('utf-8')]

    page_title = json_file['Data']['Title']
    print(page_title)
    page_head = html.part('head')
    page_head.addPart('title', page_title)
    page_body = html.part('body')
    for item in json_file['Data']:
        page_body.addPart('p', item + ': ' +str(json_file['Data'][item]))
        page_body.addPart('br')
    full_page = html.part('html')
    full_page.addPiece(page_head)
    full_page.addPiece(page_body)
    page = full_page.make()
    fileOpen2 = open("./"+index+'/'+pageTitle+'.html','w')
    fileOpen2.write(page)
