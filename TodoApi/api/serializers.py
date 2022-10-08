from rest_framework import serializers
from todo import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'date_begin',
            'date_end',
            'state'
        )
        model = models.Todo