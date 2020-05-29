from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=300)
    algorithm = models.CharField(max_length=100)
    desc = models.TextField()
    answer = models.TextField()
    note = models.CharField(max_length=200)
    pubDate = models.DateTimeField(default=timezone.now)

    class Meat:
        ordering = ('-pubDate',)
        
    def __str__(self): #可用物件實體名稱表示一段字串
        return self.question