from django.contrib import admin
from .models import Category, Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'project_type', 'category', 'status')
    list_filter = ('project_type', 'category', 'status')
    search_fields = ('title', 'location')

admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
