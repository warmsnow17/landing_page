from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')

admin.site.register(Lead, LeadAdmin)

