from rest_framework import serializers
from .models import *


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class DropdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownModel
        fields = '__all__'


class DataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = '__all__'


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunities
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'


