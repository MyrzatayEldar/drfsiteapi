from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'fullname', 'post', 'hiring_date', 'salary', 'boss')