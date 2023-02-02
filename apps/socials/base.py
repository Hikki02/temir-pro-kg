import uuid

from django.db import models
from rest_framework import serializers


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserSocialModel(BaseModel):
    title = models.CharField(max_length=225)

    class Meta:
        abstract = True


class BaseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        # you just need to create a Meta class and set the model
        # if you have the create method
        model = ...
        fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data: dict):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance: object, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class BaseSocialSerializer(BaseSerializer):
    title = serializers.CharField()

    class Meta:
        model = ...
        fields = BaseSerializer.Meta.fields + ['title', 'user', ]
