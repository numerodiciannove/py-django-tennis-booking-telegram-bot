from django.db import models
from user.models import TelegramUser


class Booking(models.Model):
    DAY_OF_WEEK = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]
    TIME_SLOTS = [
        ("05:00 - 06:00", "05:00 - 06:00"),
        ("06:00 - 07:00", "06:00 - 07:00"),
        ("07:00 - 08:00", "07:00 - 08:00"),
        ("08:00 - 09:00", "08:00 - 09:00"),
        ("09:00 - 10:00", "09:00 - 10:00"),
        ("10:00 - 11:00", "10:00 - 11:00"),
        ("11:00 - 12:00", "11:00 - 12:00"),
        ("12:00 - 13:00", "12:00 - 13:00"),
        ("13:00 - 14:00", "13:00 - 14:00"),
        ("14:00 - 15:00", "14:00 - 15:00"),
        ("15:00 - 16:00", "15:00 - 16:00"),
        ("16:00 - 17:00", "16:00 - 17:00"),
        ("17:00 - 18:00", "17:00 - 18:00"),
        ("18:00 - 19:00", "18:00 - 19:00"),
        ("19:00 - 20:00", "19:00 - 20:00"),
        ("20:00 - 21:00", "20:00 - 21:00"),
        ("21:00 - 22:00", "21:00 - 22:00"),
        ("22:00 - 23:00", "22:00 - 23:00"),
        ("23:00 - 00:00", "23:00 - 00:00"),
    ]
    EVENT_CHOICES = [
        ("tournament", "Tournament"),
        ("group_training", "Group training"),
        ("individual_training", "Individual training"),
        ("open_play", "Open play"),
    ]

    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    time = models.CharField(max_length=20, choices=TIME_SLOTS, )
    day = models.CharField(max_length=13, choices=DAY_OF_WEEK, )
    user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        related_name="user_bookings",
    )
    players_count = models.IntegerField(blank=True, null=True)
    is_repetitive = models.BooleanField(default=False)
    event = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=EVENT_CHOICES,
    )

    def __str__(self):
        return (
            f"{self.user} - ({self.day}, {self.time}, "
            f"repetitive {self.is_repetitive})"
        )

    class Meta:
        unique_together = ["day", "time"]
        ordering = ["day", "-time"]
