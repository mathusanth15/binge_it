import isodate
import ssl
from pyyoutube import Api
from youtube_search import YoutubeSearch
from binge_watch.constants import Duration

_create_unverified_https_context = ssl._create_unverified_context

API_KEY = "AIzaSyDaRory2-wGmKKJUpS2Cm19gWQ037wueAk"


class YTSearch():
    def __init__(self, api_key=API_KEY):
        self.key = api_key
        self.api = Api(api_key=self.key)

    def check_video_eligibility(self, ids, expected_type):

        like_max = {"yt_id": "", "youtube_rating": 0.0}
        for id in ids:
            video = list(self.api.get_video_by_id(video_id=id).to_dict().items())
            try:
                vid = video[5][1][0]
                duration = isodate.parse_duration(vid['contentDetails']['duration']).total_seconds()
                definition = vid['contentDetails']['definition']
                like_count = float(vid["statistics"]["likeCount"])
                dislike_count = float(vid["statistics"]["dislikeCount"])
                duration_min = Duration[expected_type][0]
                duration_max = Duration[expected_type][1]
                like_percentage = like_count / (like_count + dislike_count)
                channel_title = vid["snippet"]["channelTitle"]
                if like_percentage > like_max["youtube_rating"] and (duration_min < duration <= duration_max) and \
                        channel_title != 'YouTube Movies':
                    like_max["yt_id"] = id
                    like_max["yt_duration"] = duration
                    like_max["yt_likes"] = like_count
                    like_max["youtube_rating"] = like_percentage
                    like_max["yt_definition"] = definition
            except Exception as e:
                print("ignoring the error")
                continue
        return like_max

    def obsolete_get_stats(self, key_word, expected_type="movie", max_results=10):
        videos = list(self.api.search_by_keywords(q=key_word, search_type=["video"]).items)
        vids = [vid.to_dict()["id"]['videoId'] for vid in videos]
        ret = self.check_video_eligibility(vids, expected_type)
        print(ret)

    def get_youtube_stats(self, key_word, expected_type="movie", max_results=10):
        get_mov_stats = YoutubeSearch(key_word, max_results=max_results).to_dict()
        ids = [d['id'] for d in get_mov_stats]
        ret = self.check_video_eligibility(ids, expected_type)
        for mov in get_mov_stats:
            if mov["id"] == ret["yt_id"]:
                ret["youtube_link"] = "https://youtube.com" + mov["link"]
        return (ret)


if __name__ == "__main__":
    a = YTSearch("AIzaSyDaRory2-wGmKKJUpS2Cm19gWQ037wueAk")
    print(a.get_youtube_stats("rekka in hindi", expected_type="movie", max_results=5))
