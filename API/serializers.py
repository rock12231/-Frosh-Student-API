from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .utils import get_gravatar
from .models import (User, Profile, Experience, Education, Post, Comment)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.avatar = get_gravatar(validated_data.get('email'))
        user.save()
        Token.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class GetProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    experience = ExperienceSerializer(many=True)
    education = EducationSerializer(many=True)

    class Meta:
        model = Profile
        fields = [
            'id','user','company','website','location',
            'status', 'skills', 'bio', 'githubusername',
            'youtube', 'twitter', 'facebook', 'linkedin',
            'instagram', 'experience', 'education']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user','text','name','avatar','date','likes','post_comments']
        read_only_fields = ('post_comments',)

class CommentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name',read_only=True)
    avatar = serializers.URLField(source='user.avatar',read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id','user','post','text','date','name','avatar']
        
class GetPostSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ['id','user','text','name','avatar','date','likes','post_comments']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
        