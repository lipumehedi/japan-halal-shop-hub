from django.contrib import messages
from django.db.models import Avg, Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ShopSubmissionForm, ReviewForm
from .models import Shop, PREFECTURES, CATEGORIES

def shop_list(request):
    shops = Shop.objects.filter(is_approved=True).annotate(
        average_rating=Avg("reviews__rating", filter=Q(reviews__is_approved=True)),
        review_count=Count("reviews", filter=Q(reviews__is_approved=True)),
    )
    query = request.GET.get("q", "").strip()
    prefecture = request.GET.get("prefecture", "")
    category = request.GET.get("category", "")
    halal_status = request.GET.get("halal_status", "")
    if query:
        shops = shops.filter(
            Q(name__icontains=query) | Q(city__icontains=query) |
            Q(address__icontains=query) | Q(description__icontains=query)
        )
    if prefecture:
        shops = shops.filter(prefecture=prefecture)
    if category:
        shops = shops.filter(category=category)
    if halal_status:
        shops = shops.filter(halal_status=halal_status)
    return render(request, "shops/shop_list.html", {
        "shops": shops, "query": query, "selected_prefecture": prefecture,
        "selected_category": category, "selected_halal_status": halal_status,
        "prefectures": PREFECTURES, "categories": CATEGORIES,
        "result_count": shops.count(),
    })

def shop_detail(request, slug):
    shop = get_object_or_404(
        Shop.objects.annotate(
            average_rating=Avg("reviews__rating", filter=Q(reviews__is_approved=True)),
            review_count=Count("reviews", filter=Q(reviews__is_approved=True)),
        ),
        slug=slug, is_approved=True
    )
    reviews = shop.reviews.filter(is_approved=True)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.shop = shop
            review.save()
            messages.success(request, "Thank you! Your review is awaiting moderation.")
            return redirect(shop.get_absolute_url())
    else:
        form = ReviewForm()
    return render(request, "shops/shop_detail.html", {"shop": shop, "reviews": reviews, "form": form})

def submit_shop(request):
    if request.method == "POST":
        form = ShopSubmissionForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            # Slug is generated safely from the name; admin can adjust if a duplicate exists.
            from django.utils.text import slugify
            base_slug = slugify(shop.name) or "halal-shop"
            slug = base_slug
            suffix = 2
            while Shop.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{suffix}"
                suffix += 1
            shop.slug = slug
            shop.is_approved = False
            shop.save()
            messages.success(request, "Shop submitted! It will appear after an admin review.")
            return redirect("shop_list")
    else:
        form = ShopSubmissionForm()
    return render(request, "shops/submit_shop.html", {"form": form})
