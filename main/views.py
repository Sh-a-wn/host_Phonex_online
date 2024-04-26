from django.shortcuts import render, redirect
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
    context = {'brands': collected_data}
    return render(request, 'brands.html', context)

def phone_details(request):
    return render(request, 'phone_details.html')

def dealer_login(request):
    # redirect('add_Brand.html')
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
            # redirect('brands')
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
    return redirect('login')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def phones(request):
    return render(request, 'phones.html')

def logs(request):
    return render(request, 'loginpage.html')

# def images(request):
#     if request.method == 'POST':
#         form = ImageForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj = form.instance  # returns an instance of the image just to show the user what they have uploaded
#             return render(request, 'images.html',{'obj':obj})
        
#     else:
#         form = ImageForm()
#         img = UploadImage.objects.all()
#     return render(request, 'images.html', {'form':form, 'img':img})
    