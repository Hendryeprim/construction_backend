from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Project(models.Model):
    PROJECT_TYPES = (
        ('INTERIOR', 'Interior'),
        ('CONSTRUCTION', 'Construction')
    )
    
    title = models.CharField(max_length=200)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    location = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True) 
    design_concept = models.TextField(blank=True, null=True)
    materials_used = models.TextField(blank=True, null=True)
    timeline = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.get_project_type_display()})"

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)
    is_cover = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Image for {self.project.title}"
