from django.contrib import admin

# Register your models here.
from .models import *

#进行关联性添加
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    #下面的为嵌入的几个HeroInfo就写几
    extra = 3


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'bttile', 'bpub_date']
    list_filter = ['bttile']
    search_fields = ['bttile']
    #分页操作
    list_per_page = 10
    fieldsets = [
        ('base', {'fields': ['bttile']}),
        ('super', {'fields': ['bpub_date']})
    ]
    #BookInfo进行嵌入
    inlines = [HeroInfoInline]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
