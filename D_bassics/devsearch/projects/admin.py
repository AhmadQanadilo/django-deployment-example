from django.contrib import admin

# Register your models here.
from projects.models import project,Review,tag,AccessRecord,topic,Webpage
admin.site.register(project)
admin.site.register(Review)
admin.site.register(tag)
admin.site.register(AccessRecord)
admin.site.register(topic)
admin.site.register(Webpage)