from django.contrib import admin
from sharptest.models import BaseModel,Brand,ServiceCategory,Package,Product,Review,Store
# Register your models here.


# admin.site.register(BaseModel)
admin.site.register(Brand)
admin.site.register(ServiceCategory)
admin.site.register(Package)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Store)