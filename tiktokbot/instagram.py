import requests
import json

link = "https://www.instagram.com/reel/CmcLWqkKALH/"
def it(link):
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

	querystring = {"url": link}

	headers = {
		"X-RapidAPI-Key": "yourApiKey", #go to rapidapi.com to get Api
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	result = response.text
	rest = json.loads(result)
	return {'smth': rest['media']}

#print(it(link))