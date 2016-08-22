import os
import json
import requests
import base64
from metadata_extractor_wip import main2
from argparse import ArgumentParser


def encode_url(url):
    '''returns the encoded_url for directory creation'''
    encoded_url = base64.b64encode(url.encode('ascii'))
    if check_dir(encoded_url):
        encoded_url = (str(encoded_url).strip('b'))
    else:
        print('whoops')

    return encoded_url

def check_dir(encoded_url):
    '''checks if the encoded_url already exists as a directory'''
    status_of_dir = False

    if os.path.exists(encoded_url) == False:
        status_of_dir = True #it exists


    return status_of_dir

def main():
    parser = ArgumentParser()
    parser.add_argument('type', help = 'type OAuth to use OAuth authentication (ensure you have an OAuth.txt file in your config folder first)',
     nargs='?', const='Standard')
    args = parser.parse_args()

    username = open('../config-location/config.txt', 'r').readline().strip('\n')#location of my

    if args.type == 'OAuth':
        password = open('../config-location/oauth.txt', 'r').readline()#location of oauth file
    else:
        password_file = open('../config-location/config.txt', 'r')
        password_file.readline()
        password = password_file.readline().strip('\n')
    auth = (username, password)
    open_json = open('urls.json', 'r')
    if os.stat('urls.json').st_size > 0:
        url_json = json.load(open_json)
    url_list = url_json['URLs']
    for url in url_list:
        try:
            directory = encode_url(url)
            json_file = open('./'+directory+'./meta.json','r')
            etag = json.load(jsonFile)[url]['ETag']

            main2(url, auth, path=directory, etag = etag )
        except FileNotFoundError:
            os.mkdir(directory)
            main2(url, auth, path=directory)

main()
