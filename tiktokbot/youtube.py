import json
import requests
from urllib import parse
from urllib.parse import urlparse


def video_id(link1):

    query = urlparse(link1)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            url_parsed = parse.urlparse(link1)
            qsl = parse.parse_qs(url_parsed.query)
            return qsl['v']

        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail
    return None


link1 = "https://www.youtube.com/watch?v=_2E7HfIX_48"

def yt(link1):
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
    querystring = {"videoId": video_id(link1)}

    headers = {
		"X-RapidAPI-Key": "yourRapidApi", #go to rapidapi.com to get ApiKey
		"X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
	}

    response = requests.request("GET",url, headers=headers, params=querystring)
    result = response.text
    rest = json.loads(result)
    return {'video': rest['videos']['items'][0]['url']}



