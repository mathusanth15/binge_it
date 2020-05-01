from googleapiclient.discovery import build
from binge_watch.constants import search_engine_map
API_KEY = 'AIzaSyDaRory2-wGmKKJUpS2Cm19gWQ037wueAk'
MAX_GOOGLE_RESULTS = 10

class GoogleLib():
    def __init__(self, cse_key, api_key=API_KEY):
        self.api_key = api_key
        self.cse_key = cse_key

    def google_search(self, search_query, **kwargs):
        service = build("customsearch", "v1", developerKey=self.api_key)
        res = service.cse().list(q=search_query, cx=self.cse_key, num=MAX_GOOGLE_RESULTS,
                                 excludeTerms="Review").execute()
        return res

    def get_entity_data(self, entity_name, expected_type="movie"):
        search_query = "{} {} online".format(entity_name, expected_type)
        google_search_result = self.google_search(search_query)
        return_dict = {}
        for entity in google_search_result.get("items", []):
            if entity_name.lower() in entity['title'].lower():
                if entity["displayLink"] not in return_dict:
                    return_dict[entity["displayLink"]] = {}
                    return_dict[entity["displayLink"]]["title"] = entity["title"]
                    return_dict[entity["displayLink"]]["link"] = entity["link"]
        return return_dict

def get_entity_availability(entity_name, expected_type="movie"):
    ret = {}
    for ott in search_engine_map:
        ott_cls = GoogleLib(ott)
        entity_data = ott_cls.get_entity_data(entity_name=entity_name, expected_type=expected_type)
        ret.update(entity_data)
    return ret


if __name__ == "__main__":
    gl_res = get_entity_availability("96")
    print (gl_res)
