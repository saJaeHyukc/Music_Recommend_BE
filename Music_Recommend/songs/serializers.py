from rest_framework import serializers

from songs.models import Song, Voice, Comment

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("id","title","genre","singer","image")

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    song = serializers.StringRelatedField()
    profile_image = serializers.SerializerMethodField()
    
    def get_profile_image(self, obj):
        return obj.user.profile_image.url
    
    def get_user(self, obj):
        return obj.user.nickname
    
    class Meta:
        model = Comment
        fields = "__all__"

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)

class VoiceSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    voice_likes = serializers.StringRelatedField(many=True)
    song = serializers.StringRelatedField()
    profile_image = serializers.SerializerMethodField()
    
    def get_profile_image(self, obj):
        return obj.user.profile_image.url
    
    def get_user(self, obj): 
        return obj.user.nickname
        
    class Meta:
        model = Voice
        fields = "__all__"
        
class VoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = ('recode',)

class SongSerializer(serializers.ModelSerializer):
    song_likes = serializers.StringRelatedField(many=True)
    song_likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    voices = VoiceSerializer(many=True)
    comments_count = serializers.SerializerMethodField()
    voices_count = serializers.SerializerMethodField()

    def get_song_likes_count(self, obj) :    
        return obj.song_likes.count()
    
    def get_comments_count(self, obj) :    
        return obj.comments.count()
    
    def get_voices_count(self, obj) :    
        return obj.voices.count()

    class Meta:
        model = Song
        fields = "__all__"