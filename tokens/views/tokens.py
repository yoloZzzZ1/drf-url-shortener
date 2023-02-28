from rest_framework import generics
from tokens.serializers.api import tokens as token_s
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    post=extend_schema(summary='Создать токен', tags=['Токен']),
)
class TokenCreateAPIView(generics.CreateAPIView):
    queryset = None
    serializer_class = token_s.TokenCreateSerializer

