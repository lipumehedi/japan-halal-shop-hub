from django.contrib import admin
from .models import Shop, Review

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "prefecture", "halal_status", "is_approved", "created_at")
    list_filter = ("category", "prefecture", "halal_status", "is_approved")
    search_fields = ("name", "city", "address", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("is_approved",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("shop", "reviewer_name", "rating", "is_approved", "created_at")
    list_filter = ("rating", "is_approved")
    search_fields = ("shop__name", "reviewer_name", "comment")
    list_editable = ("is_approved",)
