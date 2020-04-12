from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    question = models.CharField(max_length=300)
    seasonCard = models.CharField(max_length=20)
    symbolCard = models.CharField(max_length=20)
    travelCard = models.CharField(max_length=20)
    explain = models.TextField()
    pubDate = models.DateTimeField(default=timezone.now)
