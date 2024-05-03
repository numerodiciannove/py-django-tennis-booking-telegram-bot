from django.contrib.auth.models import AbstractUser
from django.db import models


class TelegramUser(models.Model):
    ROLE_CHOICES = [
        ("player", "Player"),
        ("trainer", "Trainer"),
        ("admin", "Admin"),
    ]
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    role = models.CharField(
        choices=ROLE_CHOICES,
        default="player",
        max_length=20,
        blank=True,
        null=True
    )
    is_allowed = models.BooleanField(default=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    telegram_id = models.CharField(max_length=255, unique=True)
    telegram_username = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        help_text="For example '0951911919'. Without quotes",
        blank=True,
        null=True,
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
    )
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.telegram_username} - {self.first_name}"


class User(AbstractUser):
    telegram_id = models.CharField(max_length=255, null=True, blank=True)
