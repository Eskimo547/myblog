from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    # title = models.CharField(max_length=100)
    # author = models.CharField(max_length=100)
    # text = models.TextField()
    # datetime = models.DateTimeField('published')
    author = models.ForeignKey(User)
    title = models.CharField(max_length= 200)
    text = models.TextField()
    create_date = models.DateTimeField(default= timezone.now)
    published_date = models.DateTimeField(blank = True,null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title