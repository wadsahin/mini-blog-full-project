from django.contrib import admin
from .models import UserPost

# Register your models here.
class modelview(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc')

admin.site.register(UserPost, modelview)