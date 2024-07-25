import requests
import os

def get_page_content(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
    proxy_url = os.environ.get("http://fixie:W7MlfYNE7TB9k4g@velodrome.usefixie.com:80")
    
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    
    response = requests.get(url, headers=headers, proxies=proxies)
    response.raise_for_status()
    return response.content