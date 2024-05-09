from django.forms import ModelForm
from .models import Brands, Make
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
ROLES=[
    ('buyer','Buyer'),
    ('seller','Seller')
]
class BrandsForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'

class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'

class CreateNewUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class edit_Profileform(ModelForm):
    class Meta:
        model = Profile
        fields = ['role']
        widgets = {'role':forms.RadioSelect,}
