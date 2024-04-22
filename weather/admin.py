from django.contrib import admin
from weather.models import City

@admin.register(City)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']  
    search_fields = ['name']
    


