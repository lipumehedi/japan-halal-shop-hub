from django.db import models
from django.urls import reverse

PREFECTURES = [
    ("Tokyo", "Tokyo"), ("Kanagawa", "Kanagawa"), ("Chiba", "Chiba"),
    ("Saitama", "Saitama"), ("Osaka", "Osaka"), ("Aichi", "Aichi"),
    ("Fukuoka", "Fukuoka"), ("Hokkaido", "Hokkaido"), ("Other", "Other"),
]

CATEGORIES = [
    ("grocery", "Halal Grocery"), ("restaurant", "Restaurant"),
    ("butcher", "Butcher / Meat"), ("online", "Online Shop"),
    ("cosmetics", "Cosmetics"), ("other", "Other"),
]

class Shop(models.Model):
    name = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, default="grocery")
    prefecture = models.CharField(max_length=30, choices=PREFECTURES, default="Tokyo")
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    phone = models.CharField(max_length=40, blank=True)
    website = models.URLField(blank=True)
    opening_hours = models.CharField(max_length=180, blank=True)
    halal_status = models.CharField(
        max_length=20,
        choices=[("verified", "Certification checked"), ("owner", "Owner says halal"), ("unconfirmed", "Not yet confirmed")],
        default="unconfirmed",
    )
    image_url = models.URLField(blank=True, help_text="Optional image URL. Use an image you have permission to display.")
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop_detail", kwargs={"slug": self.slug})

class Review(models.Model):
    shop = models.ForeignKey(Shop, related_name="reviews", on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=80, default="Guest")
    rating = models.PositiveSmallIntegerField(choices=[(i, f"{i} star") for i in range(1, 6)])
    comment = models.TextField(max_length=1200)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.shop.name} - {self.rating}/5"
