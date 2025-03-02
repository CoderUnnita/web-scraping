import requests

url = "https://www.bbc.com/clear"

def fetchDataSaveIt(url,carry):
    r = requests.get(url)
    with open(carry, "w") as f:     
        #encoding="utf-8" this is used for unicode characters conversion, sometimes it face bugs 

        #use it while scrapping dseu website
        f.write(r.text)

fetchDataSaveIt(url, "file.html")