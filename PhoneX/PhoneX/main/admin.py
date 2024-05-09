from django.contrib import admin
from .models import Brands, Make, Profile

# Register your models here.
admin.site.register(Brands)
admin.site.register(Make)
admin.site.register(Profile)
