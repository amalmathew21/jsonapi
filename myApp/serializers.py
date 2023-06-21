from rest_framework import serializers
from .models import *
from django.core.files.storage import default_storage
from datetime import date
from django.core.files.base import ContentFile

class DateField(serializers.Field):
    def to_representation(self, value):
        return value.strftime('%Y-%m-%d')

    def to_internal_value(self, data):
        return date.fromisoformat(data)

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
    createdDate = serializers.DateField(default=date.today)
    modifiedDate = serializers.DateField(default=date.today)
    class Meta:
        model = Lead
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['createdDate'] = instance.createdDate.strftime('%Y-%m-%d')
        representation['modifiedDate'] = instance.modifiedDate.strftime('%Y-%m-%d')
        return representation


class AccountsSerializer(serializers.ModelSerializer):
    createdDate = serializers.DateField(default=date.today)
    modifiedDate = serializers.DateField(default=date.today)
    class Meta:
        model = Accounts
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['createdDate'] = instance.createdDate.strftime('%Y-%m-%d')
        representation['modifiedDate'] = instance.modifiedDate.strftime('%Y-%m-%d')
        return representation



class CustomPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except serializers.ValidationError:
            queryset = self.get_queryset()
            if isinstance(data, str) and queryset.model._meta.pk.is_string():
                try:
                    return queryset.get(pk=data)
                except queryset.model.DoesNotExist:
                    pass
            raise
class OpportunitySerializer(serializers.ModelSerializer):
    profilePhoto = serializers.SerializerMethodField()
    accountId = serializers.CharField(required=False)
    leadId = serializers.CharField(required=False)
    createdDate = serializers.DateField(default=date.today)
    modifiedDate = serializers.DateField(default=date.today)
    expectedCloseDate = serializers.DateField(format='%Y-%m-%d', required=False, allow_null=True)

    class Meta:
        model = Opportunities
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['createdDate'] = instance.createdDate.strftime('%Y-%m-%d')
        representation['modifiedDate'] = instance.modifiedDate.strftime('%Y-%m-%d')
        return representation

    def get_profilePhoto(self, instance):
        if instance.profilePhoto:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(instance.profilePhoto.url)
            return instance.profilePhoto.url
        return None

    def create(self, validated_data):
        account_id = validated_data.pop('accountId', None)
        lead_id = validated_data.pop('leadId', None)
        profile_photo = validated_data.pop('profilePhoto', None)

        if account_id:
            account_id = int(account_id)

        if lead_id:
            lead_id = int(lead_id)

        opportunity = Opportunities.objects.create(accountId_id=account_id, leadId_id=lead_id, **validated_data)

        if profile_photo:

            opportunity.profilePhoto.save(profile_photo.name, ContentFile(profile_photo.read()), save=True)

        return opportunity


class TasksSerializer(serializers.ModelSerializer):
    profilePic = serializers.SerializerMethodField()
    accountId = serializers.CharField(required=False)
    opportunityId = serializers.CharField(required=False)
    createdDate = serializers.DateField(default=date.today)
    modifiedDate = serializers.DateField(default=date.today)
    dueDate = serializers.DateField(format='%Y-%m-%d', required=False, allow_null=True)
    startDate = serializers.DateField(default=date.today)

    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['createdDate'] = instance.createdDate.strftime('%Y-%m-%d')
        representation['modifiedDate'] = instance.modifiedDate.strftime('%Y-%m-%d')
        return representation

    def get_profilePic(self, instance):
        if instance.profilePic:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(instance.profilePic.url)
            return instance.profilePic.url
        return None


    def create(self, validated_data):
        account_id = validated_data.pop('accountId', None)
        opportunity_id = validated_data.pop('opportunityId', None)
        profile_pic = validated_data.pop('profilePic', None)

        if account_id:
            account_id = int(account_id)

        if opportunity_id:
            opportunity = Opportunities.objects.get(opportunityId=int(opportunity_id))
        else:
            opportunity = None

        task = Task.objects.create(accountId_id=account_id, opportunityId=opportunity, **validated_data)

        if profile_pic:
            task.profilePic.save(profile_pic.name, ContentFile(profile_pic.read()), save=True)

        return task









class ReportsSerializer(serializers.ModelSerializer):
    accountId = serializers.CharField(required=False)
    opportunityId = serializers.CharField(required=False)
    createdDate = serializers.DateField(default=date.today)
    modifiedDate = serializers.DateField(default=date.today)

    class Meta:
        model = Report
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['createdDate'] = instance.createdDate.strftime('%Y-%m-%d')
        representation['modifiedDate'] = instance.modifiedDate.strftime('%Y-%m-%d')
        return representation

    def create(self, validated_data):
        account_id = validated_data.pop('accountId', None)
        opportunity_id = validated_data.pop('opportunityId', None)

        if account_id:
            account_id = int(account_id)

        if opportunity_id:
            opportunity = Opportunities.objects.get(opportunityId=int(opportunity_id))
        else:
            opportunity = None

        report = Report.objects.create(accountId_id=account_id, opportunityId=opportunity, **validated_data)
        return report

class NotesSerializer(serializers.ModelSerializer):
    profilePhoto = serializers.SerializerMethodField()
    accountId = serializers.CharField(required=False)
    opportunityId = serializers.CharField(required=False)
    class Meta:
        model = Notes
        fields = '__all__'


    def get_profilePhoto(self, instance):
        if instance.profilePhoto:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(instance.profilePhoto.url)
            return instance.profilePhoto.url
        return None


    def create(self, validated_data):
        account_id = validated_data.pop('accountId', None)
        opportunityId = validated_data.pop('opportunityId', None)
        profile_photo = validated_data.pop('profilePhoto', None)


        if account_id:
            account_id = int(account_id)

        if opportunityId:
            opportunityId = int(opportunityId)

        notes = Notes.objects.create(accountId_id=account_id, opportunityId=opportunityId, **validated_data)

        if profile_photo:
            notes.profilePhoto.save(profile_photo.name, ContentFile(profile_photo.read()), save=True)

        return notes
