import requests
import os
from pprint import pprint as pp


api_key = os.getenv("GIPHY_KEY")

base_url = "http://api.giphy.com/v1/gifs/search?"
trend_url = "http://api.giphy.com/v1/gifs/trending?"

def make_url(query,limit_count):
    url = base_url+"q={}&api_key={}&limit={}".format(query,api_key,limit_count)
    return url
    
def make_trend_url(limit_count):
    url = trend_url+"api_key={}&limit={}".format(api_key,limit_count)
    return url

def json_parsing(json_file):
    result = []
    titles=[]
    sources=[]
    for values in json_file["data"]:
        tmp_url = values.get("images").get("original").get("url")
        tmp_title = values.get("title")
        tmp_source = values.get("source_tld")
        result.append(tmp_url)
        titles.append(tmp_title)
        sources.append(tmp_source)
    return result,titles,sources


def send_request(query="Cat",limit_count=10):
    url = make_url(query,limit_count)
    res = requests.get(url)
    res_json=res.json()
    return res_json
    
def trend_request(limit_count=10):
    url=make_trend_url(limit_count)
    res=requests.get(url)
    res_json=res.json()
    return res_json

def download_files(query,urls,limit_count=10):
    
    for idx,url in enumerate(urls):
        res=requests.get(url)
        with open("./download/{}_{:2d}.jpg".format(query,idx),'w') as f:
            f.write(res.content)
    

if __name__ == "__main__":
    query = input()
    json_file = send_request(query,10)
    urls,titles,sources = json_parsing(json_file)
    download_files(query,urls,5)
    
    


# Giphy와 imgur에서 해당 쿼리로 스크랩해와서 다운로드 받아주는 프로그램.
# 실행창에서 까지!