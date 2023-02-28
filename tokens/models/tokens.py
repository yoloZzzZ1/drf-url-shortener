from django.db import models


class Token(models.Model):

    """
    Token storage model
    """

    full_url = models.URLField(
        unique=True,
    )

    short_url = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    requests_count = models.IntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = (
            '-created_at',
        )

    def __str__(self):
        return f'{self.full_url} ({self.pk})'