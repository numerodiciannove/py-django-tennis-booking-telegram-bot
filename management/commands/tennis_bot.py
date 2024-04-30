from django.core.management.base import BaseCommand
from telegream_bot.main import main


class Command(BaseCommand):
    """Command to start tennis bot"""

    def handle(self, *args, **options):
        self.stdout.write("Tennis bot started...")

        main()

        self.stdout.write(self.style.SUCCESS("Bot available!"))
