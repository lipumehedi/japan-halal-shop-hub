
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from shops.models import Shop


class Command(BaseCommand):
    help = "Add real shop listings from published Yokohama tourism information."

    def handle(self, *args, **options):
        shops = [
            {
                "name": "AGM Trading Halal Food Shop",
                "category": "grocery",
                "prefecture": "Kanagawa",
                "city": "Yokohama",
                "address": (
                    "1-1-16, 2F, Tsunashima Nishi, "
                    "Kohoku-ku, Yokohama, Kanagawa"
                ),
                "phone": "045-546-6817",
                "website": "http://www.agmtrading.com/",
                "description": (
                    "A halal food shop in Yokohama offering groceries, "
                    "spices, frozen foods and imported food products. "
                    "Confirm current products and halal information "
                    "directly with the shop."
                ),
                "halal_status": "unconfirmed",
            },
            {
                "name": "Hari Rasai",
                "category": "restaurant",
                "prefecture": "Kanagawa",
                "city": "Yokohama",
                "address": (
                    "1-6-17, 2F, Tsunashima-nishi, "
                    "Kohoku-ku, Yokohama, Kanagawa"
                ),
                "phone": "045-545-9887",
                "website": "",
                "description": (
                    "Sri Lankan restaurant listed in the Yokohama "
                    "Official Visitors Guide. Contact the restaurant "
                    "to confirm its current menu and halal practices."
                ),
                "halal_status": "unconfirmed",
            },
            {
                "name": "DELHI Dining",
                "category": "restaurant",
                "prefecture": "Kanagawa",
                "city": "Yokohama",
                "address": (
                    "1F, Kannai JS Building, 207 Yamashita-cho, "
                    "Naka-ku, Yokohama, Kanagawa"
                ),
                "phone": "045-633-9393",
                "website": (
                    "https://tabelog.com/kanagawa/"
                    "A1401/A140104/14045727"
                ),
                "description": (
                    "Indian restaurant in central Yokohama. The "
                    "Yokohama tourism guide lists halal dishes and "
                    "ingredients. Confirm current details directly."
                ),
                "halal_status": "unconfirmed",
            },
            {
                "name": "New Alibaba",
                "category": "restaurant",
                "prefecture": "Kanagawa",
                "city": "Yokohama",
                "address": (
                    "Palais Kannai 1F, 1-2-1 Aioi-cho, "
                    "Naka-ku, Yokohama, Kanagawa"
                ),
                "phone": "045-651-0388",
                "website": "https://alibaba-japan.owst.jp/",
                "description": (
                    "Turkish restaurant in Yokohama. The Yokohama "
                    "tourism guide describes halal-friendly food "
                    "options. Contact the restaurant to verify "
                    "current ingredients and preparation practices."
                ),
                "halal_status": "unconfirmed",
            },
        ]

        for item in shops:
            slug = slugify(item["name"])

            Shop.objects.update_or_create(
                slug=slug,
                defaults={
                    **item,
                    "is_approved": True,
                },
            )

            self.stdout.write(
                self.style.SUCCESS(f"Added or updated: {item['name']}")
            )

        self.stdout.write(
            self.style.SUCCESS("Finished importing 4 shop listings.")
        )
