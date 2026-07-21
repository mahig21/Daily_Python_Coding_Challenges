#29-04-26
"""
Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.

* The query string begins after the "?",
* each parameter is separated by "&",
* each key/value pair is separated by "="
"""
def parse_url_query(url):
    info=url[url.index("?")+1:]
    info=info.split("&")
    dict_a={}
    for i in info:
        pair=i.split("=")
        dict_a[pair[0]]=pair[1]
    return dict_a
dict_a=parse_url_query("https://freecodecamp.org/learn?skill=programming&language=python")
print(dict_a)