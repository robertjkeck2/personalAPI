from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

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
    """
    John has a few emails and phone numbers. Find out all the ways to get in touch with him.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class EducationViewSet(viewsets.ModelViewSet):
    """
    John is a lifelong learner. See all of his previous educational achievements.
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    """
    John has worked at some great companies. Explore John's work experience.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class InterestViewSet(viewsets.ModelViewSet):
    """
    John has many interests outside of work. Take a look at what he does in his free time.
    """
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class LinkViewSet(viewsets.ModelViewSet):
    """
    John collects links he thinks are interesting. Check some of his favorites out.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class MeViewSet(viewsets.ModelViewSet):
    """
    There's a lot of information about John here. For a quick summary, hit this endpoint.
    """
    queryset = Me.objects.all()
    serializer_class = MeSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    John loves to work on side projects. Thumb through his code.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    John writes about topics he finds fascinating. Read some of his posts. 
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SkillViewSet(viewsets.ModelViewSet):
    """
    John works hard to learn new skills and practice existing ones. Analyze his expertise.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SocialViewSet(viewsets.ModelViewSet):
    """
    John is active on social media. To follow him, find all of his handles.
    """
    queryset = Social.objects.all()
    serializer_class = SocialSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAdminUser]
