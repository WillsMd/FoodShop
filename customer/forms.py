from django import forms
from setuptools import setup, find_packages
setup(
    name= 'models',
    packages = find_packages()
    )

from .models import Item

class AddForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('created_by',
        'title', 'image', 'description', 'price', 'pieces', 'instructions', 'labels', 'label_colour', 'slug')
