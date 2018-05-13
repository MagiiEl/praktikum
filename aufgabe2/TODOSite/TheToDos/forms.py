# -*- coding: utf-8 -*-
from django import forms

class ToDoForm(forms.Form):
    description = forms.CharField(label='text', max_length=300)
    deadline = forms.CharField(label='deadline', max_length= 100)
    percent = forms.IntegerField(label='percent')
