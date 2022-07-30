from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Product, Review


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    reviews = Review.objects.filter(product=product).order_by('-id')
    print (reviews)
    return render(request, 'store/products/single.html', {'product': product, 'reviews': reviews})

def test(request):
    return "Hello there"

def Rate(request, slug):
    if request.method == "POST":        
        print("saving", slug)
        product = get_object_or_404(Product, slug=slug, in_stock=True)
        subject = request.POST.get('subject')
        review = request.POST.get('review')
        rate = request.POST.get('rate')
        user = request.user
        Review(user=user, product=product, subject=subject, review=review, rate=rate).save()
        return redirect('/' + slug) 