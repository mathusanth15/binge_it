from binge_watch.entity.base import Serializable, Entity

class Movie(Serializable, Entity):
    def __init__(self, payload):
        super(Movie, self).__init__()
        Entity.__init__(self)
        self.payload = payload

    def populate_attribs(self):
        self.title = self.payload.get("title")
        self.imdb_id = self.payload.get("imdb_id")
        self.imdb_rating = self.payload.get("imdb_rating")
        self.actors = self.payload.get("actors")
        self.rated = self.payload["rated"]
        self.duration = self.payload["runtime"]
        self.genre = self.payload["genre"]
        self.director = self.payload["director"]
        self.plot = self.payload["plot"]
        self.language = self.payload["language"]
        self.poster = self.payload["poster"]
        self.release_year = self.payload["year"]
        self.poster = self.payload["poster"]
        self.youtube_id = self.payload["yt_id"]
        self.youtube_link = self.payload["youtube_link"]
        self.youtube_likes = self.payload["yt_likes"]
        self.youtube_rating = self.payload["youtube_rating"]
        self.youtube_video_quailty = self.payload["yt_definition"]
        self.youtube_duration = self.payload["yt_duration"]
        self.ott_providers = self.payload["ott_providers"]

        try:
            self.rotten_tomato_rating = self.payload["ratings"][1]["value"]
        except Exception as e:
            print ("Not able to find rotten tomatoes rating...")

