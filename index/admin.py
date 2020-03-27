from django.contrib import admin

# Register your models here.

from .models import Avatar,Project,Linkexchange,Hr,Seo


class AvatarAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'image')
    list_filter = ['update_date']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    list_filter = ['update_date']

class LinkexchangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

class HrAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SeoAdmin(admin.ModelAdmin):
    fields = ['title', 'keywords','desc']
    list_display = ('title','keywords')


admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Linkexchange, LinkexchangeAdmin)
admin.site.register(Hr, HrAdmin)
admin.site.register(Seo, SeoAdmin)