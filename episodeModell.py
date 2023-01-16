# a class that makes a python dictionary out of an episode payload from Buzzsprout
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