class Entity():
    def __init__(self):
        self.name = None
        self.youtube_id = None
        self.youtube_trailer_link = None
        self.youtube_movie_link = None
        self.youtube_likes = None
        self.youtube_dislikes = None
        self.duration = None
        self.definition = None

class Movie(Entity):
    def __init__(self):
        super(Movie, self).__init__()
        self.type = "movie"

class WebSeries(Entity):
    def __init__(self):
        super(WebSeries, self).__init__()
        self.type = "webseries"