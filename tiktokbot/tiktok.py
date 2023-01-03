import json

import requests

link = "https://vm.tiktok.com/ZMFnohMVX/"
def tk(link):

	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url": link}

	headers = {
		"X-RapidAPI-Key": "yourApiKey", #go to rapidapi.com to get Api
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	result = response.text
	rest = json.loads(result)
	return {'video':rest['video'][0]}


