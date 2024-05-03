from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_filter = ["event", "is_repetitive", "day", "user"]


admin.site.register(Booking, BookingAdmin)
