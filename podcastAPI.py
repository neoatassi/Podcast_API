import requests
import json

class Episode:

  def __init__(self, data):

    self.id = data['id']
    self.title = data['title']
    self.audio_url = data['audio_url']
    self.artwork_url = data['artwork_url']
    self.description = data['description']
    self.summary = data['summary']
    self.artist = data['artist']
    self.tags = data['tags']
    self.published_at = data['published_at']
    self.duration = data['duration']
    self.hq = data['hq']
    self.magic_mastering = data['magic_mastering']
    self.guid = data['guid']
    self.inactive_at = data['inactive_at']
    self.episode_number = data['episode_number']
    self.season_number = data['season_number']
    self.explicit = data['explicit']
    self.private = data['private']
    self.total_plays = data['total_plays']

buzzsproutUrl = "https://www.buzzsprout.com/api/2109700/episodes.json"

buzzsproutPayload={}
buzzsproutHeaders = {
  'Authorization': 'Token token=b2fdc92fb3503f0cee9d9d9ed4c15f91',
  'token': 'b2fdc92fb3503f0cee9d9d9ed4c15f91'
}

response = requests.request("GET", buzzsproutUrl, headers=buzzsproutHeaders, data=buzzsproutPayload).json()

episodes = []
counter = 0
for item in response:
  episodes.append(Episode(item))
  counter += 1



print(episodes[0].title, episodes[0].total_plays, episodes[0].id)