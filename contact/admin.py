from django.contrib import admin
from .models import *


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'fullname', 'created_date', 'is_read_by_admin']
    list_editable = ['is_read_by_admin']


admin.site.register(ContactUs, ContactUsAdmin)
