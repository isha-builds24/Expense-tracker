from django.shortcuts import render,redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request,'myapp/landing.html')
    if request.method == "POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            new_expense = expense.save(commit=False)
            new_expense.user = request.user
            new_expense.save()
            return redirect('index')

    expenses = Expense.objects.filter(user=request.user)
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    expense_form = ExpenseForm()

    today = datetime.date.today()
    yearly_sum = expenses.filter(date__gt=today - datetime.timedelta(days=365)).aggregate(Sum('amount'))['amount__sum'] or 0
    monthly_sum = expenses.filter(date__gt=today - datetime.timedelta(days=30)).aggregate(Sum('amount'))['amount__sum'] or 0
    weekly_sum = expenses.filter(date__gt=today - datetime.timedelta(days=7)).aggregate(Sum('amount'))['amount__sum'] or 0

    daily_sums = expenses.values('date').order_by('date').annotate(sum=Sum('amount'))
    categorical_sums = expenses.values('category').annotate(sum=Sum('amount'))

    return render(request, 'myapp/dark-modern-index.html', {
        'expense_form': expense_form,
        'expenses': expenses,
        'total_expenses': total_expenses,
        'yearly_sum': yearly_sum,
        'monthly_sum': monthly_sum,
        'weekly_sum': weekly_sum,
        'daily_sums': daily_sums,
        'categorical_sums': categorical_sums,
    })
# @login_required
# def edit(request,id):
#     expense =Expense.objects.get(id=id)
#     expense_form=ExpenseForm(instance=expense)
#     if request.method=="POST":
#         form=ExpenseForm(request.POST,instance=expense)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     return render(request,'myapp/modern-edit.html',{'expense_form':expense_form})

# @login_required
# def delete(request,id):
#     if request.method=="POST":
#         expense= Expense.objects.get(id=id)
#         expense.delete()
#     return redirect('index')

@login_required
def edit(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    expense_form = ExpenseForm(instance=expense)
    if request.method == "POST":
        expense_form = ExpenseForm(request.POST, instance=expense)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('index')
    return render(request, 'myapp/modern-edit.html', {'expense_form': expense_form})

@login_required
def delete(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    if request.method == "POST":
        expense.delete()
    return redirect('index')

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.save())
        return redirect('index')
    return render(request, 'myapp/register.html', {'form': form})