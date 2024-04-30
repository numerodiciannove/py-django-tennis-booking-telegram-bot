from django.contrib import admin
from user.models import User, TelegramUser

admin.site.register(User)
admin.site.register(TelegramUser)
