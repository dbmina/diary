from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): 
    # id는 자동 추가
    title = models.CharField(max_length=256)
    content = models.TextField()
    satisfaction= models.CharField(max_length=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self): 
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title