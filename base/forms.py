from dataclasses import field
from django.forms import ModelForm,ModelChoiceField
from django import forms
# from .models import main

# class HomeForm(ModelForm):
#     class Meta:
#         model = main
#         fields = ['train_no']
        # train_no = forms.ModelChoiceField(queryset=main.objects.values_list('train_no').distinct().order_by('train_no'))