import glob
import makeHTML as html
import json
import base64

listt=glob.glob("./'IGh0d*'")

for index in listt:
    file_open = open('./'+index+'/meta.json', 'r')
    json_file = json.load(file_open)[base64.b64decode(index).decode('utf-8')]
    page_title = json_file['Data']['Title']

    page_head = html.part('head')
    page_head.addPart('title', page_title)
    page_head.addPart('link',
    attributes={'rel':'stylesheet','href':'../css/ref.css'})

    page_body = html.part('body')
    page_body.addPart('h1', page_title)
    #page_body.addPart('h2', 'by ' + json_file['author'])
    for item in json_file['Data']:
        if json_file['Data'][item] != '':
            page_body.addPart('p', '<b>' + item + '</b>'+ ': ' +str(json_file['Data'][item]), attributes = {'class':'indent-left'})
    full_page = html.part('html')
    full_page.addPiece(page_head)
    full_page.addPiece(page_body)
    page = full_page.make()
    write_file = open("./"+index+'/'+page_title+'.html','w')
    write_file.write(page)
    write_file.close()
