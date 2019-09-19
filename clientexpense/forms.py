from django import forms
from .models import Client, Expense
import re


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'active']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        match = re.match("^[a-zA-Z ]+$", name)
        if not match:
            raise forms.ValidationError("Client name should be in characters")
        return name


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount',
                  'currency',
                  'title',
                  'description']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        match = re.match("^[a-zA-Z ]+$", title)
        if not match:
            raise forms.ValidationError("Title should be in characters")
        return title
