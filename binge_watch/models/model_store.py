from binge_watch.models.models import EntityInformation
from binge_watch.models.models import YouTube
from django.http import HttpResponse
from binge_watch.entity.entity_class import Entity

def store_entity(entity):
    input = entity.data
    entity_name = input.get("name")
    year = input.get("year")
    if not entity_name:
        return HttpResponse("Please provide mandatory fields entity_name")
    en = Entity()
    entity = en.populate_entity(entity_name, year)
    entity_entry = EntityInformation(uuid=entity.uuid,
                                     name=entity.title,
                                     entity_type=entity.entity_type,
                                     genre=entity.genre,
                                     language=entity.language,
                                     dubbed_langs=entity.dubbed_langs,
                                     available_medium=entity.available_medium,
                                     ott_links=entity.ott_providers,
                                     actors=entity.actors,
                                     imdb_id=entity.imdb_id,
                                     imdb_rating=entity.imdb_rating,
                                     rotten_tomato_rating=entity.rotten_tomato_rating,
                                     our_rating=entity.our_rating,
                                     duration=entity.duration,
                                     description=entity.plot,
                                     release_year=entity.release_year,
                                     poster= entity.poster
                                     )
    yt_entity = YouTube(
        uuid=entity.uuid,
        youtube_id= entity.youtube_id,
        youtube_trailer_link = entity.youtube_trailer_link,
        youtube_link = entity.youtube_link,
        youtube_likes = entity.youtube_likes,
        youtube_rating = entity.youtube_rating,
        youtube_video_quality = entity.youtube_video_quailty,
        youtube_duration = entity.youtube_duration
    )
    entity_entry.save()
    yt_entity.save()