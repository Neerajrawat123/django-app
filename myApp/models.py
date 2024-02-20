from django.db import models

# Create your models here.

from django.db import models

class MarketInsight(models.Model):
    end_year = models.IntegerField(null=True)
    intensity = models.IntegerField(null=True)
    sector = models.CharField(max_length=100, null=True)
    topic = models.CharField(max_length=100, null=True)
    insight = models.TextField(null=True)
    url = models.URLField(null=True)
    region = models.CharField(max_length=100, null=True)
    start_year = models.IntegerField(null=True)
    impact = models.TextField(null=True)
    published = models.DateTimeField(null=True)
    country = models.CharField(null=True,max_length = 100)
    relevance = models.IntegerField(null=True)
    pestle = models.CharField(null=True,max_length=100)
    source = models.CharField(null=True,max_length=100)
    title = models.CharField(null=True,max_length=255)
    likelihood = models.IntegerField(null=True)
    added = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.title
