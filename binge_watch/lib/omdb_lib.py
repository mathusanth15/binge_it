import omdb
API_KEY = 'db5aad81'

class OMDB():
    def __init__(self, api_key=API_KEY):
        self.api_key = api_key
        omdb.set_default('tomatoes', True)
        self.client = omdb.OMDBClient(apikey=API_KEY)

    def get_movie_details_from_name_year(self, name, year=None):
        if name == "":
            raise Exception(" Name is mandatory to be passed")
        args = {"title": name}
        if year:
            args[year] = year
        movie = self.client.get(**args)
        return movie


if __name__ == "__main__":
    o = OMDB()
    print (o.get_movie_details_from_name_year("96"))
