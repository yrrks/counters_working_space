from django.db import models
from django.conf import settings


class UserTheme(models.Model):
    THEME_CHOICE=[
        ('white', 'светлая'),
        ('dark', 'темная'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='theme'
    )

    theme = models.CharField(
        max_length=10,
        choices=THEME_CHOICE,
        default='white'
    )
