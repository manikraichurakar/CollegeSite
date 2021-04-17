from rest_framework.serializers import ModelSerializer
from .models import *
from restapi.serializers import StudentSer
from rest_framework import serializers

class DepartmetnSer(ModelSerializer):
    stud = StudentSer(source='StudentSer_set')
    class Meta:
        model = Department
        fields = ['deptid','name','no_of_students','stud']