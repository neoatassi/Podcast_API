import requests
import json
import csv
import pandas as pd
import episodeModell as ep

'''
Following code is configured to the API of the podcast hosting service BUZZSPROUT.
A USER_ID and a TOKEN for the podcast should be provided for the script to work
'''

# Podcast User ID
USER_ID = ''

# API access token
TOKEN = ''

# Podcast Host URL to get all episodes
HOST_URL = 'https://www.buzzsprout.com/api/' + USER_ID + '/episodes.json'

HEADERS = {
  'Authorization': 'Token token=' + TOKEN,
  'token': TOKEN
}
PAYLOAD={}


def getEpisodes(UserId, token, HostURL):
  # HTTP request to get all episodes
  RESPONSE = requests.request("GET", HOST_URL, headers=HEADERS, data=PAYLOAD).json()

  # Export podcast data to .csv and .xlsx files
  podcastCSV = pd.DataFrame(RESPONSE).to_csv('podcast.csv', index=None)
  podcastExcel = pd.DataFrame(RESPONSE).to_excel('podcast.xlsx', index=None)

  # save payload as a list of episodes
  episodes = []
  for item in RESPONSE:
      episodes.append(ep.Episode(item))

  return episodes


episodes = getEpisodes(UserId=USER_ID, token=TOKEN, HostURL=HEADERS)