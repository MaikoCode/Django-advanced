from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . import forms
from django.views.generic import View


class LoginPageView(View):
    template_name = 'authentification/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})
        


def logout_user(request):
    logout(request)
    return redirect('login')

def login_page(request):
    form = forms.LoginForm()
    message = " "
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']    
            )
            if user is not None:
                login(request, user)
                return redirect('home')
                message = f'Bonjour, {user.username}! Vous êtes connecté'
            else:
                message = 'Identifiants incorrects'
    return render(request, 'authentification/login.html', context={'form': form, 'message': message})

# def login_page(request):
#     form = forms.LoginForm()
#     message = ''
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 message = f'Bonjour, {user.username}! Vous êtes connecté.'
#             else:
#                 message = 'Identifiants invalides.'
#     return render(request, 'authentification/login.html', context={'form': form, 'message': message})