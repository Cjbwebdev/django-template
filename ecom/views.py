from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth import logout
from .models import Product

def home(request):
    products = Product.objects.all()  # Ensure you're fetching all products here
    return render(request, 'ecom/home.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)  # Retrieve the product
    return render(request, 'ecom/product_detail.html', {'product': product})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'ecom/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('ecom:index')

def cart_view(request):
    cart_items = request.session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    return render(request, 'ecom/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if the product is already in the cart
    for item in cart:
        if item['id'] == product_id:
            item['quantity'] += 1
            break
    else:
        cart.append({
            'id': product_id,
            'name': product.name,
            'price': product.price,
            'quantity': 1
        })
    
    request.session['cart'] = cart
    return redirect('cart')

def product_list(request):
    products = Product.objects.all()  # Make sure this query retrieves all products
    return render(request, 'ecom/home.html', {'products': products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if the product is already in the cart
    for item in cart:
        if item['id'] == product_id:
            item['quantity'] += 1
            break
    else:
        cart.append({
            'id': product_id,
            'name': product.name,
            'price': product.price,
            'quantity': 1
        })
    
    request.session['cart'] = cart
    return redirect('home') 