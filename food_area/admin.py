from django.contrib import admin
from food_area.models import Area
# Register your models here.

class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'area_name','zip_code']
    list_display_links = ['area_name']
    list_filter = ['area_name']
    search_fields = ['id','area_name']

admin.site.register(Area, AreaAdmin)