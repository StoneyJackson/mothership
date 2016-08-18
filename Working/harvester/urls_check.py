import requests
import sys
import json
import os
from argparse import ArgumentParser



def get_urls(url, user, repo_name, auth, urls_json):
    url_list = []
    repo_list = []

    github_request = requests.get(url, auth = auth)

    if github_request.status_code == 200: #successful request because repo exists
        urls_request = requests.get("https://raw.github.com/%s/%s/master/urls.md" % (user, repo_name))
        if urls_request.status_code == 200:
            if os.stat('urls.json').st_size > 0:
                if urls_json['ETag'] != None: #no etag? if possible need to check
                    if urls_json['ETag'] != urls_request.headers['ETag'].strip('\"'):
                        etag = (urls_request.headers['ETag'].strip('\"'))
                        urls = str(urls_request.content).strip('-').split(' ')
                        urls = urls[1:]  #skip the first line its irrelevant and something github includes
                        for url in urls:
                            url = url.strip('\n')
                            url = url.rstrip().rstrip()

                            url_list += [url]
                            url_split = url.split('/')
                            item = url_split[4].split('.')
                            repo = item[0]
                            repoList += [repo]

                    else:
                        print('Request has the same ETag exiting since no changes have been made.')
                        sys.exit()
            else:
                etag = (urls_request.headers['ETag'].strip('\"'))
                urls = (urls_request.content.decode('utf-8').split('\n'))

                urls_copy = urls[:len(urls)-1]  #skip the last line its
                #print(urlscopy[])
                for url in urls_copy:
                    url = url.strip('-')

                    url_list += [url]
                    url_split = url.split('/')
                    item = url_split[4].split('.')
                    repo = item[0]
                    repo_list += [repo]

    else:
        print(github_request.status_code)
        print("invalid url entered")
        sys.exit()

    return url_list, repo_list, etag
def parse_dict(url_list, repo_list, etag):
    urls_dict = {}
    urls_dict['ETag'] =  etag

    urls_dict['URLs'] = url_list
    #for repo in repoList:
        #repo_dict[repo] = url_list[repoList.index(repo)]
    return urls_dict
def write_json(repo_dict):
    json_file = open('urls.json','w')
    json_data = json.dumps(repo_dict)
    json_file.write(json_data)
    json_file.close()
    print("Json file created successfully!")

def main():
    parser = ArgumentParser()
    parser.add_argument('url', help = 'the url to the git repo containing a urls.md')
    parser.add_argument('type', help = 'type OAuth to use OAuth authentication (ensure you have an OAuth.txt file in your config folder first)', nargs='?', const='Standard')
    args = parser.parse_args()


    try:
        open_json = open('urls.json', 'r')
        if os.stat('urls.json').st_size > 0:
            url_json = json.load(open_json)
        open_json.close()
    except FileNotFoundError:
        url_json = open('urls.json', 'w')
    username = open('../config-location/config.txt', 'r').readline().strip('\n')#location of my

    if args.type == 'OAuth':
        password = open('../config-location/oauth.txt', 'r').readline()#location of oauth file
    else:
        password_file = open('../config-location/config.txt', 'r')
        password_file.readline()
        password = password_file.readline().strip('\n')
    #I wanted to the input url to be a ".git" url but I couldn't find any reference to that within the repos, interestingly
    #enough its in the json returned from the GET request
    input_url = args.url
    auth = (username, password)
    parts_of_url = input_url.split('/')
    user = parts_of_url[3]
    repo_name = parts_of_url[4]
    #URLS.md should in exist in the root
    request_url = ("https://api.github.com/repos/%s/%s/contents/urls.md/" % (user, repo_name))
    url_list, repo_list, etag = get_urls(request_url, user, repo_name, auth, url_json)
    urls_dict = parse_dict(url_list, repo_list, etag)
    write_json(urls_dict)


main()
