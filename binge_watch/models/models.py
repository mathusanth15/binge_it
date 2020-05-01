import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
import datetime

from binge_watch import constants

class JSONField(models.TextField):
    """
    JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly.
    Django snippet #1478

    example:
        class Page(models.Model):
            data = JSONField(blank=True, null=True)


        page = Page.objects.get(pk=5)
        page.data = {'title': 'test', 'type': 3}
        page.save()
    """

    def to_python(self, value):
        if value == "":
            return {}

        try:
            if isinstance(value, str):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def from_db_value(self, value, *args):
        return self.to_python(value)

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return {}
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return value

class EntityInformation(models.Model):
    # Type of the entity, like: Web Series, Movie, Short Film
    uuid = models.CharField(max_length=128, unique=True, primary_key=True)
    entity_type = models.CharField(max_length=256)
    # Entity public attribs
    name = models.CharField(max_length=256)
    genre = models.CharField(max_length=15, null=True)
    language = models.CharField(max_length=256, null=True)
    dubbed_langs = models.CharField(max_length=256, null=True)
    available_medium = models.CharField(max_length=256, null=True)
    ott_links = JSONField()
    actors = models.CharField(max_length=256, null=True)
    imdb_id = models.CharField(max_length=25, null=True)
    imdb_rating = models.CharField(max_length=20, null=True)
    rotten_tomato_rating = models.CharField(max_length=20, null=True)
    our_rating = models.CharField(max_length=20, null=True)
    duration = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=256, null=True)
    release_year = models.CharField(max_length=20, null=True)
    poster = models.CharField(max_length=256, null=True)

class YouTube(models.Model):
    uuid = models.CharField(max_length=128, unique=True, primary_key=True)
    youtube_id = models.CharField(max_length=25, null=True)
    youtube_trailer_link = models.CharField(max_length=256, null=True)
    youtube_link = models.CharField(max_length=256, null=True)
    youtube_likes = models.IntegerField(null=True)
    youtube_rating = models.FloatField(null=True)
    youtube_video_quality = models.CharField(max_length=25, null=True)
    youtube_duration = models.IntegerField(null=True)




