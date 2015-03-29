import json
import requests
import re as regex
import gui

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
                #for z in y:
                    #if z["semantic_url"]:
                if "semantic_url" in y:
                    if "daily-programming-thread" in y["semantic_url"]:
                        print(y["sub"])
                        print(y["no"])
                        return str(y["no"])

if __name__ == "__main__":
    board = "g"
    catalog_url = "https://a.4cdn.org/g/catalog.json"
    thread = "https://a.4cdn.org/"
    catalog = Get().fetch_url(catalog_url).json()
    t_number = Get().find_t_number(catalog)
    threadurl = thread + board + "/thread/" + t_number + ".json"
    content = Get().fetch_url(threadurl).json()

    #with open("thread.json", mode='w', encoding='utf-8') as file:
    #    json.dump(content, file, indent=6)

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

    gui.root.mainloop()
