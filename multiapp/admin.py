from django.contrib import admin
from multiapp.models import multi_insert_data
# Register your models here.

class multi_insert_dataAdmin(admin.ModelAdmin):
	list_display=('name','age','gender','did','course')

admin.site.register(multi_insert_data,multi_insert_dataAdmin)

