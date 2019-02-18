from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from api import views


router = routers.DefaultRouter()
router.register(r'contact', views.ContactViewSet)
router.register(r'education', views.EducationViewSet)
router.register(r'experience', views.ExperienceViewSet)
router.register(r'interests', views.InterestViewSet)
router.register(r'links', views.LinkViewSet)
router.register(r'me', views.MeViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'socials', views.SocialViewSet)
router.register(r'users', views.UserViewSet)
schema_view = get_swagger_view(title='Robert John Keck API',)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
]