from django.contrib import admin
from about_us.models import About_Us

class About_UsAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_head', 'title_desc')

admin.site.register(About_Us,About_UsAdmin)
