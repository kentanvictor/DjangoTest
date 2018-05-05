from django.contrib import admin

# Register your models here.
from .models import *

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','bttile','bpub_date']
    list_filter = ['bttile']
    search_fields = ['bttile']
    list_per_page = 1
    fieldsets = [
        ('base',{'fields':['bttile']}),
        ('super',{'fields':['bpub_date']})
    ]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
