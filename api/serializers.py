from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
	Contact,
    Education,
    Experience,
	Interest,
    Link,
    Me,
    Project,
    Post,
    Skill,
    Social
)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Education
		fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Experience
		fields = '__all__'

class InterestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Interest
		fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Link
		fields = '__all__'

class MeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Me
		fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skill
		fields = '__all__'

class SocialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Social
		fields = '__all__'