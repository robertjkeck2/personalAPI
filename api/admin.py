from django.contrib import admin

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

admin.site.register(Contact)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Interest)
admin.site.register(Link)
admin.site.register(Me)
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Skill)
admin.site.register(Social)
