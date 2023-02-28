from rest_framework import serializers
from tokens.models.tokens import Token
from tokens.services.short_url_generate import generate_short_url
from django.db import IntegrityError


class TokenCreateSerializer(serializers.ModelSerializer):

    short_url = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    requests_count = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Token
        fields = (
            'id',
            'full_url',
            'short_url',
            'created_at',
            'requests_count',
            'is_active'
        )

    def create(self, validated_data):
        short_url = generate_short_url()
        validated_data['short_url'] = short_url
        try:
            instance = super().create(validated_data) 
        except IntegrityError:
            raise IntegrityError
        return instance
    