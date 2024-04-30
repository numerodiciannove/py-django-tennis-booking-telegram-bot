from django.db import models


class Court(models.Model):
    COURT_SURFACE_CHOICES = [
        ("hard_court", "Hard Court"),
        ("clay_court", "Clay Court"),
        ("grass_court", "Grass Court"),
        ("carpet_court", "Carpet Court"),
        ("other", "Other"),
    ]
    DISTRICT_CHOICES = [
        ("shevchenkivskyi", "Shevchenkivskyi"),
        ("holosiivskyi", "Holosiivskyi"),
        ("pecherskyi", "Pecherskyi"),
        ("obolonskyi", "Obolonskyi"),
        ("podilskyi", "Podilskyi"),
        ("darnytskyi", "Darnytskyi"),
        ("solomianskyi", "Solomianskyi"),
        ("desnianskyi", "Desnianskyi"),
        ("dniprovskyi", "Dniprovskyi"),
        ("sviatoshynskyi", "Sviatoshynskyi"),
    ]

    name = models.CharField(unique=True, max_length=150)
    street = models.CharField(max_length=150, null=True, blank=True)
    coordinate_latitude = models.FloatField(
        max_length=15,
        help_text=(
            "For example '50.469611'. Without quotes."
        ),
        null=True,
        blank=True
    )
    coordinate_longitude = models.FloatField(
        max_length=15,
        help_text=(
            "For example '30.602457'. Without quotes"
        ),
        null=True,
        blank=True
    )
    surface_type = models.CharField(
        max_length=20,
        choices=COURT_SURFACE_CHOICES,
        null=True,
        blank=True
    )
    neighborhood = models.CharField(
        max_length=50,
        choices=DISTRICT_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}"
