from django.contrib import admin

from meta.models import MetaData
from meta.models import StudentMetaData

# Register your models here.
admin.site.register(MetaData)
admin.site.register(StudentMetaData)
