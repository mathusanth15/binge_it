# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from binge_watch.models import model_store
from binge_watch.models.models import EntityInformation

class ViewObject(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        model_store.store_entity(request)
        message = "Entity {} loaded successfully".format(request)
        return JsonResponse({'message': message})

    def list(self, request, *args, **kwargs):
        all_entries = EntityInformation.objects.all()
        msg = [dict(name=obj.name) for obj in all_entries]
        return JsonResponse({"message": msg})