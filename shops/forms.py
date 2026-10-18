from django import forms
from .models import Shop, Review

class ShopSubmissionForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            "name", "category", "prefecture", "city", "address", "description",
            "phone", "website", "opening_hours", "halal_status", "image_url",
        ]
        widgets = {"description": forms.Textarea(attrs={"rows": 4})}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["reviewer_name", "rating", "comment"]
        widgets = {"comment": forms.Textarea(attrs={"rows": 3})}
