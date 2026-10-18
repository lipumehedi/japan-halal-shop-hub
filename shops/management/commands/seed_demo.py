from django.core.management.base import BaseCommand
from django.utils.text import slugify
from shops.models import Shop

class Command(BaseCommand):
    help = "Add clearly labelled fictional demo shops for local development."

    def handle(self, *args, **options):
        demo = [
            dict(name="Demo Halal Market Tokyo", category="grocery", prefecture="Tokyo", city="Shinjuku",
                 address="Demo address — replace before publishing", description="Fictional demo listing for testing the directory. Verify all products and certification directly with the shop.", halal_status="unconfirmed"),
            dict(name="Demo Halal Foods Yokohama", category="grocery", prefecture="Kanagawa", city="Yokohama",
                 address="Demo address — replace before publishing", description="Fictional demo listing for testing search and filters. This is not a real shop recommendation.", halal_status="unconfirmed"),
            dict(name="Demo Halal Restaurant Osaka", category="restaurant", prefecture="Osaka", city="Osaka",
                 address="Demo address — replace before publishing", description="Fictional demo listing. Do not rely on this sample for real-world halal status.", halal_status="unconfirmed"),
        ]
        for item in demo:
            slug = slugify(item["name"])
            Shop.objects.update_or_create(slug=slug, defaults={**item, "is_approved": True})
        self.stdout.write(self.style.SUCCESS("Added 3 fictional demo listings. Replace or delete before launch."))
