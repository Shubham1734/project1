from django.contrib import admin
from .models import Image
# Register your models here.
@admin.register(Image)
class imageadmin(admin.ModelAdmin): 
    li = ['id','Photo','date']
