from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Playlist
from songs.models import Song

from .serializers import PlaylistCreateSerializer, PlaylistSerializer, PlaylistDetailSerializer, PlaylistSerializer

class PlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    
    #플레이리스트 전체 리스트
    def get(self, request):
        playlist = Playlist.objects.filter(user=request.user.id)
        serializer = PlaylistSerializer(playlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #플레이리스트 생성
    def post(self, request):
        serializer = PlaylistCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PlaylistDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    #플레이리스트에 노래 여러 개 추가(serializer를 못씀...)
    # def post(self, request, playlist_id):
    #     song_list = list(request.data["id"]) #id값으로 전달
    #     playlist_detail = get_object_or_404(Playlist, id=playlist_id).playlist_detail #해당 플레이리스트 가져옴
    #     exist_list = [] #중복 곡
    #     add_list =[] #추가 곡
    #     for i in range(len(song_list)):
    #         song = Song.objects.get(id=song_list[i])
    #         if playlist_detail.filter(id=song_list[i]).exists():
    #             exist_list.append(song) #중복 곡 존재하면 exist_list에 추가
    #         else:
    #             add_list.append(song) #없으면 add_list에 추가
    #             playlist_detail.add(song) #해당 플레이리스트에 곡 추가
                
    #     if len(exist_list) == 1 & len(add_list) == 0: 
    #         return Response(f"'{exist_list[0].singer}의 {exist_list[0].title}'(이)가 플레이리스트에 이미 추가되어있음", status=status.HTTP_200_OK) 
        
    #     elif len(exist_list) == 1 & len(add_list) == 1:
    #         return Response(f"'{exist_list[0].singer}의 {exist_list[0].title}'(이)가 플레이리스트에 이미 추가되어있며 '{add_list[0].singer}의 {add_list[0].title}'곡이 추가되었음", status=status.HTTP_200_OK) 
        
    #     elif len(exist_list) == 1 & len(add_list) > 1:
    #         return Response(f"'{exist_list[0].singer}의 {exist_list[0].title}'(이)가 플레이리스트에 이미 추가되어있며 {len(add_list)}곡이 추가되었음 ", status=status.HTTP_200_OK) 

    #     elif len(exist_list) > 1 & len(add_list) == 0:
    #         return Response(f"'{exist_list[0].singer}의 {exist_list[0].title}' 외 {len(exist_list)-1} 곡이 플레이리스트에 이미 추가되어있음", status=status.HTTP_200_OK)
        
    #     elif len(exist_list) > 1:
    #         return Response(f"'{exist_list[0].singer}의 {exist_list[0].title}' 외 {len(exist_list)-1} 곡이 플레이리스트에 이미 추가되어있으며 {len(add_list)}곡이 추가되었음", status=status.HTTP_200_OK) 
        
    #     return Response(f"플레이리스트에 노래 {len(add_list)}곡이 추가됨", status=status.HTTP_200_OK)

    #플레이리스트 상세페이지
    def get(self, request, playlist_id):
        playlist = get_object_or_404(Playlist, id=playlist_id )
        serializer = PlaylistDetailSerializer(playlist)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    #플레이리스트 수정
    def put(self, request, playlist_id):
        playlist = get_object_or_404(Playlist, id=playlist_id )
        if request.user == playlist.user:
            serializer = PlaylistCreateSerializer(playlist, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data , status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("접근 권한 없음", status=status.HTTP_403_FORBIDDEN)
    
    #플레이리스트 삭제
    def delete(self, request, playlist_id):
        playlist = get_object_or_404(Playlist, id=playlist_id )
        if request.user == playlist.user:
            playlist.delete()
            return Response(status=status.HTTP_200_OK)
        return Response("접근 권한 없음", status=status.HTTP_403_FORBIDDEN)

#플레이리스트 노래 추가
class PlaylistSongView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, song_id, playlist_id):
        song = get_object_or_404(Song, id=song_id)
        playlist_detail = get_object_or_404(Playlist, id=playlist_id).playlist_detail
        if playlist_detail.filter(id=song.id).exists():
            playlist_detail.remove(song.id)
            return Response({"message":"플레이리스트에 노래 제거 "}, status=status.HTTP_200_OK)
        else:
            playlist_detail.add(song.id)
            return Response({"message":"플레이리스트에 노래 추가 "}, status=status.HTTP_200_OK)
