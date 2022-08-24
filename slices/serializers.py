from rest_framework import serializers

from .models import Articles




class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['author', 'title', 'body']

        #does author field give full acess to usermanage in calls to model