#!/usr/bin/env python3
import sys
import os
from urllib.parse import urlsplit, urlunsplit
from urllib.parse import unquote_plus
from atlassian import Confluence

def obtain_confluence_pat(path='~/.ConfluencePAT'):
    confluence_PAT_filename = os.path.expanduser(path)
    confluence_PAT = None
    if os.path.exists(confluence_PAT_filename):
        with open(confluence_PAT_filename, "r") as pat_file:
            confluence_PAT = pat_file.readline()
    else:
        from getpass import getpass
        confluence_PAT = getpass(prompt="Confluence Personal Access Token")

    return confluence_PAT

def process_tags(page_id, cf_instance=None, tags=[]):
    for tag in tags:
        cf_instance.set_page_label(page_id, tag)

def add_tags_to_page_children(page_id, cf_instance=None, tags=[]):
    page_children = cf_instance.get_child_pages(page_id=page_id)
    for children in page_children:
        process_tags(children['id'], cf_instance=cf_instance, tags=tags)

def get_id_for_url(url="", cf_instance=None):
    url_items = url.split("/")
    try:
        space_start = url_items.index("display") + 1
        space = url_items[space_start]
        title = url_items[-1]
        page_id = cf_instance.get_page_id(space, unquote_plus(title))
    except ValueError:
        page_id = url_items[-1].split("=")[-1]
    return page_id

def is_valid_url(the_url):
    result = True
    try:
        split_url = urlsplit(the_url)
        if split_url.scheme not in ('http', 'https'):
            result = False
    except:
        result = False
    return result
    
def base_url(the_url):
    result = ''
    split_url = urlsplit(the_url)
    result = f"{split_url.scheme}://{split_url.netloc}/"
    return result

if __name__ == '__main__':
    cf_page_url = input("Provide page URL: ")
    if (is_valid_url(cf_page_url)):
        
        base_cf_url = base_url(cf_page_url)
        cf = Confluence(base_cf_url, token = obtain_confluence_pat())
        
        page_id  = get_id_for_url(cf_page_url,cf_instance=cf)
        
        tags = []
        while True:
            tag = input("Tag to add (empty to stop): ")
            if tag != "":
                tags.append(tag)
            else:
                break
        
        add_tags_to_page_children(page_id, cf_instance=cf, tags=tags)