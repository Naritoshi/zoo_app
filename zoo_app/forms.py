from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#未使用   
class UploadFileForm(forms.Form):
    file = forms.FileField(label="動物の画像を選択してください")
    file.attrs={'class': 'waves-effect waves-light btn'}

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='名字を入力')
    last_name = forms.CharField(max_length=30, required=True, help_text='名前を入力')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )