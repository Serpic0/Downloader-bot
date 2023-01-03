import requests
import json

link = "https://www.facebook.com/reel/1187362698778788"
def fb(link):
    url = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "yourApiKey", #go to rapidapi.com to get ApiKey
        "X-RapidAPI-Host": "facebook-reel-and-video-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    rest = json.loads(result)
    return {'videofb': rest['links']['Download High Quality']}
#print(fb(link))