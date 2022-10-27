from django.contrib import admin
from contacts.models import UserContacts

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','mobile','message')
    list_display_links = ('id',)
    list_editable = ('username','email','mobile','message')

admin.site.register(UserContacts,ContactsAdmin)
