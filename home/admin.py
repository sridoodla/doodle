from django.contrib import admin

from .models import Project, Tag, Link


class LinkInline(admin.TabularInline):
    model = Link


class TagAdmin(admin.ModelAdmin):
    model = Tag


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    filter_horizontal = ('tags',)
    inlines = [LinkInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
