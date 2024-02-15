from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    deletetime = models.DateTimeField(null=True)
    
    def delete(self, using=None, keep_parents=False):
        self.deletetime = timezone.now()
        self.save()
        return self