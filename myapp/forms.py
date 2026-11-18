# from django.forms import ModelForm
# from .models import Expense

# class ExpenseForm(ModelForm):
#     class Meta:
#         model = Expense
#         fields = ('name','amount','category')


# class ExpenseForm(forms.ModelForm):
#     class Meta:
#         model = Expense
#         fields = [
#             'name', 
#             'amount', 
#             'category', 
#             'date', 
#             'description', 
#             'payment_method'
#         ]
#         # Adding widgets to make the date field render nicely as a calendar picker in HTML
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'amount': forms.NumberInput(attrs={'class': 'form-control'}),
#             'category': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'payment_method': forms.Select(attrs={'class': 'form-control'}),
#         }

from django.forms import ModelForm, DateInput, TextInput, NumberInput, Textarea, Select
from .models import Expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = [
            'name', 
            'amount', 
            'category', 
            'date', 
            'description', 
            'payment_method'
        ]
        widgets = {
            'date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'amount': NumberInput(attrs={'class': 'form-control'}),
            'category': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'payment_method': Select(attrs={'class': 'form-control'}),
        }