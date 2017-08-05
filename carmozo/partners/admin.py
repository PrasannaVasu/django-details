# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib import admin
from .models import PartnersDetails,ContactDetails,Venue
# Register your models here.

class ContactInline(admin.TabularInline):
 model = ContactDetails

class PartnersAdmin(admin.ModelAdmin):
    inlines = (ContactInline, )
    list_display = ('name', 'type', 'code')
    search_fields = ['address',]
	
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ( 'name', 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )
admin.site.register(PartnersDetails,PartnersAdmin)
admin.site.register(ContactDetails)
admin.site.register(Venue)