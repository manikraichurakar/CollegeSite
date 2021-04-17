from .models import Course
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import Serializer,BaseSerializer
from rest_framework import serializers
class course_serialize(BaseSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    sem = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return super(course_serialize,self).create(**validated_data)

    def update(self, instance, validated_data):
        return super(course_serialize,self).update(**validated_data)
