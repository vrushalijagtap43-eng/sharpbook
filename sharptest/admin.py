from django.contrib import admin
from sharptest.models import BaseModel,Brand,ServiceCategory,Package
# Register your models here.


# admin.site.register(BaseModel)
admin.site.register(Brand)
admin.site.register(ServiceCategory)
admin.site.register(Package)