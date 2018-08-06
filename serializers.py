from classcast.search_fetch.models import chapter
from rest_framework import serializers

class chapterlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = chapter
       