from django.db import models
from django.urls import reverse

class Article(models.Model):
    name = models.CharField(max_length=96)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])
