from binge_watch.lib.omdb_lib import OMDB
from binge_watch.lib.youtube_lib import YTSearch
from binge_watch.lib.google_lib import get_entity_availability
from binge_watch.constants import EntityType

class Entity():
    def __init__(self):
        self.omdb = OMDB()
        self.yt = YTSearch()

    def populate_entity(self, entity, year, language="hindi"):
        movie = self.omdb.get_movie_details_from_name_year(entity, year)
        if year:
            entity = entity + " {}".format(year)
        type = movie["type"]
        keyword = "{} {} in {}".format(entity, type, language)
        entity = EntityType[type]
        movie_links = get_entity_availability(entity, type)
        yt_link = self.yt.get_youtube_stats(keyword, expected_type=type)
        yt_link["ott_providers"] = movie_links
        movie.update(yt_link)
        en_ong = entity(movie)
        en_ong.entity_type = type
        en_ong.populate_attribs()
        return en_ong




