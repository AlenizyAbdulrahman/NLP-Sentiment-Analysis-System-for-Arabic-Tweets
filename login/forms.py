from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordChangeForm



class main_search(ModelForm):
    class Meta:
        model = search
        fields = ['title','number']

class customer_info(ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"inputEmail3"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"inputEmail3"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"inputEmail3"}))
    # password = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"inputPassword3", "type":"password" , "name":"pass"}))

    class Meta:
        model = User
        fields = ["email",'first_name',"last_name"]


class CreateNewUser(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "type":"text", "name":"Username", "placeholder":"أسم المستخدم"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "type":"text", "name":"email", "placeholder":"البريد الالكتروني"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "name":"password", "id":"password",  "type":"password", "placeholder":"كلمة المرور"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={"class":"input100" ,"type":"password", "name":"confirm_password", "id":"confirm_password" , "placeholder":"تأكيد كلمة المرور"}))
    class Meta:
        model = User
        fields = ["username","email","password1", "password2"]

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={"class":"input100", "type":"email", "placeholder":"البريد الالكتروني"}))

class UserPasswordchangeForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordchangeForm, self).__init__(*args, **kwargs)
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "name":"password", "id":"password",  "type":"password", "placeholder":"كلمة المرور"}))
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={"class":"input100" ,"type":"password", "name":"confirm_password", "id":"confirm_password" , "placeholder":"تأكيد كلمة المرور"}))


class changePassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(changePassword, self).__init__(*args, **kwargs)
    old_password = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "name":"password", "id":"password",  "type":"password", "placeholder":"كلمة المرور القديمة"}))
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={"class":"input100" ,"type":"password", "name":"confirm_password", "id":"confirm_password" , "placeholder":"كلمة المرور الجديدة"}))
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={"class":"input100" ,"type":"password", "name":"confirm_password", "id":"confirm_password" , "placeholder":"تأكيد كلمة المرور"}))