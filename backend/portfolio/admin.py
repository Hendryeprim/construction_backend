from django.contrib import admin
from .models import Category, Project, ProjectImage, Enquiry

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'project_type', 'category', 'status')
    list_filter = ('project_type', 'category', 'status')
    search_fields = ('title', 'location')

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'interest', 'created_at')
    list_filter = ('interest', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('created_at',)

admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Enquiry, EnquiryAdmin)
