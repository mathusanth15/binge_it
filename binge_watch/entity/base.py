import uuid
class Serializable(object):
    def __init__(self):
        self.uuid = str(uuid.uuid4())


class Entity():
    def __init__(self):
        self.title = None
        self.youtube_id = None
        self.youtube_trailer_link = None
        self.youtube_link = None
        self.youtube_likes = None
        self.youtube_rating = None
        self.youtube_video_quailty = None
        self.duration = None
        self.definition = None
        self.entity_type = None
        self.genre = None
        self.language = None
        self.dubbed_langs = None
        self.available_medium = None
        self.actors = None
        self.imdb_id = None
        self.imdb_rating = None
        self.rotten_tomato_rating = None
        self.metacritic_rating = None
        self.our_rating = None
        self.duration = None
        self.plot = None
        self.rated = None
        self.release_year = None
        self.director = None
        self.poster = None
        self.ott_providers = None