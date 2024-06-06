from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms



class UserForm(forms.Form):
    username = forms.CharField(label="账号", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码', widget=CaptchaTextInput(attrs={'class': 'form-control'}))

