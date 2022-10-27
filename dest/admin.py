from django.contrib import admin
from dest.models import Dest

class DestAdmin(admin.ModelAdmin):
    list_display = ('id','dest_img','dest_place','dest_desc')
    list_display_links = ('id',)
    list_editable = ('dest_img','dest_place','dest_desc')

admin.site.register(Dest,DestAdmin)
