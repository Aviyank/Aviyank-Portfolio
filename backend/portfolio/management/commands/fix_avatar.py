from django.core.management.base import BaseCommand
from portfolio.models import Profile
import os

class Command(BaseCommand):
    help = 'Update profile avatar to use an existing image in media/avatars/'

    def handle(self, *args, **options):
        avatars_dir = os.path.join('media', 'avatars')
        if not os.path.exists(avatars_dir):
            self.stdout.write(self.style.ERROR('avatars directory does not exist.'))
            return
        files = [f for f in os.listdir(avatars_dir) if os.path.isfile(os.path.join(avatars_dir, f))]
        if not files:
            self.stdout.write(self.style.ERROR('No avatar images found in avatars directory.'))
            return
        profile = Profile.objects.first()
        if not profile:
            self.stdout.write(self.style.ERROR('No profile found.'))
            return
        # Pick the first available image
        profile.avatar = f"avatars/{files[0]}"
        profile.save()
        self.stdout.write(self.style.SUCCESS(f'Profile avatar updated to {files[0]}'))
