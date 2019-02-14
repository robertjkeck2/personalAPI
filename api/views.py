import json
import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser

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
from .serializers import (
    ContactSerializer,
    EducationSerializer,
    ExperienceSerializer,
	InterestSerializer,
    LinkSerializer,
    MeSerializer,
    ProjectSerializer,
    PostSerializer,
    SkillSerializer,
    SocialSerializer,
    UserSerializer
)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class MeViewSet(viewsets.ModelViewSet):
    queryset = Me.objects.all()
    serializer_class = MeSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAdminUser]
