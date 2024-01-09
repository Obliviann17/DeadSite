from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import UserCreationForm, LoginForm

def index(request):
    #Вывод по 1 товару с каждой категории
    products = Product.objects.order_by('cat', 'name').distinct('cat')

    context = {
        'products': products,
    }


    return render(request, 'main/index.html', context=context)
def product_page(request, product_slug):
    product_details = get_object_or_404(Product, slug=product_slug)
    small_images = product_details.additional_images.all()

    context = {
        'product_details': product_details,
        'small_images': small_images,
    }

    return render(request, 'main/product_page.html', context=context)

def about_us(request):
    return render(request, 'main/about-us.html')

def contact_us(request):
    return render(request, 'main/contact.html')

def products(request):
    main_products = Product.objects.all().order_by('name')
    cats = Category.objects.all()


    context = {
        'main_products': main_products,
        'cats': cats,
    }

    return render(request, 'main/products.html', context=context)

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me', False)

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(1814400)
                return redirect('home')

    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'main/login.html', context=context)

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    form.fields['username'].widget.attrs['placeholder'] = 'Username'
    form.fields['password1'].widget.attrs['placeholder'] = 'Password'
    form.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

    context = {
        'form': form,
    }
    return render(request, 'main/registration.html', context=context)

def logout_page(request):
    logout(request)
    return redirect('home')