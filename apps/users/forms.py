# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)
    captcha = captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})

#找回密码
class ForgetForm(forms.Form):
    email = forms.EmailField()
    captcha = captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})

class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)
