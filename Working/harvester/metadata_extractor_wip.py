import requests
import json
import sys
from argparse import ArgumentParser


def get_num_pages(url, auth):
    '''find out the maximum number of pages needed to traverse for a given repo'''
    request = requests.get(url, auth = auth)

    try:
        last_page = request.headers['Link'].split(';')[1].split('?')[1].split('=')[1]
        num_pages = int(last_page.strip('>'))
    except KeyError:  #some of these requests wont have pagination because they're only one page
        num_pages = 0
    return num_pages

#need to use a different URL
def get_data(user, repo_name, auth, data_type):
    '''get different types of data depending on which data type is requested i.e. contributors,stars, etc'''
    repo_url = ("https://api.github.com/repos/"+user+"/"+repo_name+"/"+data_type)
    num_pages = get_num_pages(repo_url, auth)
    data_list = []
    if num_pages == 0: #do a non paginated request
        repo_url =  "https://api.github.com/repos/"+user+"/"+repo_name+"/"+data_type
        data_request = requests.get(repo_url, auth = auth)
        data_json = data_request.json()
        for data in data_json:
            if data_type != 'commits':
                if data['login'] not in data_list: #contributors and watchers have this
                    data_list+=[data['login']]
            else:
                data_list += [data]
    else:
        for page in range(num_pages+1):
            repo_url =  "https://api.github.com/repos/"+user+"/"+repo_name+"/"+data_type+"?page="+ str(page)
            data_request = requests.get(repo_url, auth = auth)
            data_json = data_request.json()
            for data in data_json:
                if data_type != 'commits':
                    if data['login'] not in data_list:
                        data_list+=[data['login']]
                else:
                    data_list += [data]

    return len(data_list)
def get_metadata(user, repo_name, auth, **kwargs):
    '''get the metadata for a given repo'''
    metadata_url = ("https://api.github.com/repos/%s/%s" % (user, repo_name))
    if 'checkstat' in kwargs:
        etag_to_check = kwargs['checkstat']
        if etag_to_check == requests.get(metadata_url, auth = auth).headers['etag'].strip('\"'):
            print('ETag is the same no updating necessary')
            sys.exit()
        else: #etag is not the same so update
            metadata_request = requests.get(metadata_url, auth = auth)
            metadata_json = metadata_request.json()
            title = metadata_json["name"]
            description = metadata_json["description"]
            print(description)
            stars = metadata_json["stargazers_count"]
            forks = metadata_json["forks_count"]
            meta_etag = metadata_request.headers['etag'].strip('\"')
            metadata = {}

            metadata["Title"] = title
            metadata["Repo Description"] = description
            metadata["Stars"] = stars
            metadata["Number of forks"] = forks
            return metadata, meta_etag
    else: #no etag to pass since it doesn't exist
        metadata_request = requests.get(metadata_url, auth = auth)
        metadata_json = metadata_request.json()
        title = metadata_json["name"]
        description = metadata_json["description"]
        stars = metadata_json["stargazers_count"]
        forks = metadata_json["forks_count"]
        meta_etag = metadata_request.headers['etag'].strip('\"')
        metadata = {}

        metadata["Title"] = title
        metadata["Repo Description"] = description
        metadata["Stars"] = stars
        metadata["Number of forks"] = forks
        return metadata, meta_etag
def get_last_commit(user, repo, auth):
    '''get the last commit made to the repo'''
    url = 'https://api.github.com/repos/%s/%s/git/refs/heads/master' % (user, repo)
    master = requests.get(url, auth = auth)
    commit_object_url = master.json()['object']['url']
    last_commit = requests.get(commit_object_url, auth = auth).json()
    last_commit_dict = {}
    last_commit_dict['Author'] = last_commit['author']['name']
    last_commit_dict['Message'] = last_commit['message']
    return last_commit_dict
def parse_dict(repo_url,metadata_dict, contributors, commits, last_commit_dict, watchers, etag):
    '''parse all the metadata into dictionaries that will be written to a json'''
    repodict = {}
    repodict['ETag'] = etag
    metadict = {}
    metadata_dict['Contributors'] = contributors
    metadata_dict['Commits'] = commits
    metadata_dict['Watchers'] = watchers
    repodict['Data'] = metadata_dict
    repodict['Last Commit'] = last_commit_dict
    metadict[repo_url] = repodict
    return metadict


def write_json(meta_dict, **kwargs):
    '''write metadata to json'''
    if ('path' in kwargs):
        print('path specified')
        path = kwargs['path']
        json_file = open('./'+str(path)+'/meta.json', 'w')
    else:
        print('no path specified')
        json_file = open('meta.json', 'w')
    json_data = json.dumps(meta_dict)
    json_file.write(json_data)
    json_file.close()
    print("Json file created successfully!")

def main2(input_url, auth, **kwargs):
    '''for the purpose of importing into harvester the main2 is the actual "main"'''
    parts_of_url = input_url.split('/')
    user = parts_of_url[3]
    repo_name = parts_of_url[4].split('.')[0]
    if 'etag' in kwargs:
        etag_to_check = kwargs['etag']
        metadata_dict, etag = get_metadata(user,repo_name,auth, checkstat = etag_to_check)
    else:
        metadata_dict, etag = get_metadata(user,repo_name,auth )

        watchers = get_data(user, repo_name, auth, 'subscribers')
        contributors = get_data(user, repo_name, auth, 'contributors')

    if metadata_dict is None:
        print('ETag is the same no updating necessary')
        sys.exit()
    last_commit_dict = get_last_commit(user, repo_name, auth)
    commits = get_data(user, repo_name, auth, 'commits')
    repo_dict = parse_dict(input_url, metadata_dict, contributors, commits, last_commit_dict, watchers, etag)
    if 'path' in kwargs:
        write_json(repo_dict, path = kwargs['path'])
    else:
        write_json(repo_dict)
def main():
    '''main for running the program standalone'''
    parser = ArgumentParser()
    parser.add_argument('url', help = 'the url to the git repo containing a urls.md')
    parser.add_argument('type', help = 'type OAuth to use OAuth authentication (ensure you have an OAuth.txt file in your config folder first)', required = False)
    args = parser.parse_args()

    username = open('../config-location/config.txt', 'r').readline().strip('\n')#location of my
    if args.type == 'OAuth':
        password = open('../config-location/oauth.txt', 'r').readline()#location of oauth file
    else:
        password_file = open('../config-location/config.txt', 'r')
        password_file.readline()
        password = password_file.readline().strip('\n')
    auth = (username, password)
    input_url = args.url
    main2(input_url, auth)

if __name__ == "__main__":
    main()
