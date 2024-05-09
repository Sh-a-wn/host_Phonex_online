from django.urls import path
from . import views

urlpatterns = [
    path("",  views.startup_page, name='startup'),
    path('startup/', views.startup_page, name='startup'),
    path('home/', views.homepage, name='homepage'),
    path("brands/", views.brands, name="brands"),
    path('dealer_login/', views.dealer_login, name='dealer_login'),
    path('user_login/', views.user_login, name="user_login"),
    path('add-Brand/', views.addBrand, name='addBrand'),
    path('register/', views.register, name='register'),
    path('sell_phone/', views.sell_phone, name="sell_phone"),
    path('phone_details/', views.phone_details, name="phone_details"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginPage, name='login'),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('phones/', views.phones, name="phones"),
    path('logout/', views.logoutUser, name="logout"),
    path('logs/', views.logs, name='logs'),
    path('profile/',views.edit_profile, name="profile"),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('adjust-cart/<str:product_id>/', views.adjust_cart, name='adjust_cart'),
]