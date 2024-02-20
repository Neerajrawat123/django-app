from myApp.models import MarketInsight
from rest_framework import serializers


class MarketInsightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarketInsight
        fields = ['end_year', 'intensity', 'sector', 'topic', 'insight', 'url', 'region', 'start_year', 'impact', 'published', 'country', 'relevance', 'pestle', 'source', 'title', 'likelihood', 'added']


