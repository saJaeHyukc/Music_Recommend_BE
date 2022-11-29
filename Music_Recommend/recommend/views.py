from django.shortcuts import get_list_or_404
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView

import random

from songs.models import Song
from recommend.serializers import SongListSerializer
from recommend.recommend_function import get_recommendations    

class SongListView(APIView):
    def get(self, request):
        song_list = get_list_or_404(Song)
        listserializer = SongListSerializer([random.choice(song_list) for i in range(12)], many=True)
        return Response(listserializer.data, status=status.HTTP_200_OK)

class SongRecommendView(APIView):
    def post(self, request, song_id):
        slt_song = get_list_or_404(Song, id=song_id)
        print(slt_song[0].pk)
        rcm_list = get_recommendations(slt_song[0].pk)
        print(rcm_list)
        return Response(rcm_list, status=status.HTTP_200_OK)