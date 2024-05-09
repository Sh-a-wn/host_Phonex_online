from django.shortcuts import render, redirect, get_object_or_404
from .models import Brands,Profile, Make
from .forms import BrandsForm, CreateNewUser, edit_Profileform, MakeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def startup_page(request):
    return render(request, 'home.html')

def homepage(request):
    return render(request, 'homepage.html')

def brands(request):
    collected_data = Make.objects.all()
    cart = request.session.get('cart', {})
    total_items = sum(item['quantity'] for item in cart.values())  # total number of items in the cart
    context = {
        'brands': collected_data,
        'cart': cart,
        'total_items': total_items
    }
    return render(request, 'brands.html', context)


def phone_details(request):
    return render(request, 'phone_details.html')

def dealer_login(request):
    return render(request, 'dealer_login.html')

def user_login(request):
    form = CreateNewUser()

    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/homepage')


    context = {'form' : form}
    return render(request, 'registerpage.html', context)

def addBrand(request):
    form = MakeForm()

    if request.method == 'POST':
        form = MakeForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('brands')
    context = {'form': form}
    return render(request, 'add_Brand.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    else:
        form = CreateNewUser()
        if request.method == 'POST':
            form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created successfully')

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')


        context = {'form' : form}
        return render(request, 'register.html', context)
    
    
def edit_profile(request):
    profile = Profile.objects.get(user = request.user)
    form = edit_Profileform()
    if request.method == "POST":
        form = edit_Profileform(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully selected role")
    context = {'form':form}
    return render(request, 'profile_radio.html', context)


@login_required(login_url='login')
def sell_phone(request):
    form = MakeForm()

    if request.method == 'POST':
        form = MakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'sell_phone.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('{{request.META.HTTP_REFERER}}')  # returns the user to the page they were on before being redirected
    
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user != None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Invalid username or password')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('startup')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def phones(request):
    return render(request, 'phones.html')

def logs(request):
    return render(request, 'loginpage.html')

def add_to_cart(request, product_id):
    product = get_object_or_404(Make, id=product_id)
    cart = request.session.get('cart', {})

    # Product ID might need to be a string in session dictionary keys
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
    else:
        cart[product_id_str] = {
            'name': product.name,
            'price': product.price,
            'quantity': 1
        }

    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER'))


def view_cart(request):
    cart = request.session.get('cart', {})
    total = 0

    for item in cart.values():
        total += item['price'] * item['quantity']

    context = {'cart': cart,'total': total}
    return render(request, 'cart.html', context)
    

def adjust_cart(request, product_id):
    action = request.POST.get('action')
    cart = request.session.get('cart', {})

    if product_id in cart:
        if action == 'increase':
            cart[product_id]['quantity'] += 1
        elif action == 'decrease':
            if cart[product_id]['quantity'] > 1:
                cart[product_id]['quantity'] -= 1
            else:
                del cart[product_id]  # Remove the item if quantity is 1

    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', 'view_cart'))  # Redirect back to the cart or product page