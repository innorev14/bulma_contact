from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_no', 'service', 'url_type', 'url', 'content', 'created_at')
    list_filter = ('created_at',)

