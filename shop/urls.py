from django.urls import path
from setuptools import setup, find_packages
setup(
    name= 'views',
    packages = find_packages()
    )
from . import views
app_name = 'shop'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
