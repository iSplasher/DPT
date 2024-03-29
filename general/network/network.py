import json
import requests

class Get:
    def __init__(self):
        pass

    def fetch_url(self, url):
        "Downloads the desired url"
        try:
            content = requests.get(url)
            return content
        except:
            return print("Not valid URL")

    def find_t_number(self, catalog):
        "Finds and returns the DPT thread number"
        for x in catalog:
            threads = x["threads"]
            for y in threads:
                if "semantic_url" in y:
                    if "daily-programming-thread" in y["semantic_url"]:
                        #print(y["sub"])
                        #print(y["no"])
                        return str(y["no"])

def get_posts():
    "Returns thread number and posts ->  t_number, posts"
    board = "g"
    catalog_url = "https://a.4cdn.org/g/catalog.json"
    thread = "https://a.4cdn.org/"
    catalog = Get().fetch_url(catalog_url).json()
    t_number = Get().find_t_number(catalog)
    threadurl = thread + board + "/thread/" + t_number + ".json"
    content = Get().fetch_url(threadurl).json()

    #conatins posts in this hiearchy:
    #    [
    #        {
    #              OP, thread info  
    #            }
    #        {
    #                reply 1
    #            }
    #        ]
    posts = content["posts"]
    return t_number, posts