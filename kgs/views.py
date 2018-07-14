# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from kgs.models import *
from django.shortcuts import render

class KgsListView(APIView):

    def get(self, request):
        key=Kgs.objects.filter(used=False).first()
        Kgs.objects.filter(key=key.key).update(used=True)
        print key.key
        return Response({'message': key.key})

    def post(self, request):
        keys = Kgs.create_short_keys()
        return Response({'message': '1000 keys successfully created'})

