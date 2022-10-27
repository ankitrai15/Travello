from django.contrib import admin
from home.models import HomeImage

class HomeImageAdmin(admin.ModelAdmin):
    list_display = ('home_img',)

admin.site.register(HomeImage,HomeImageAdmin)
