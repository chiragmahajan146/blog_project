from django.contrib import admin
from first_app.models import topic,accessrecord,webpage
admin.site.register(accessrecord)
# Register your models here.
admin.site.register(topic)
admin.site.register(webpage)
