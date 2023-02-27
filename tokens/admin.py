from django.contrib import admin
from tokens.models.tokens import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'full_url',
        'short_url',
        'created_at',
        'requests_count',
        'is_active',
    )

    list_display_links = (
        'id',
        'short_url',
    )

    search_fields = (
        'full_url',
        'short_url',
    )

    ordering = (
        '-created_at',
    )