from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from FOOD.shop.forms import NewUSerForm
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view
def signup_view(request):
    if request.method == 'POST':
        form = NewUSerForm(data=request.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customer:home')
    else:
        form = NewUSerForm()
    return render(request, 'shop/signup.html', { 'form': form })

@api_view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('customer:home')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', { 'form': form })

@api_view
def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('/')