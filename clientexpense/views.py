from django.shortcuts import render
from .forms import ClientForm, ExpenseForm
from .models import Client, Expense
from datetime import datetime
from django.contrib import messages
# Create your views here.


def client_home(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        record = Client(timestamp=datetime.now(),
                        name=form.cleaned_data.get('name'),
                        active=form.cleaned_data.get('active'))
        record.save()
        messages.success(request, 'successfully added client!')
    queryset = Client.objects.all().order_by('-timestamp')
    context = {
        "form": form,
        "queryset": queryset
    }
    return render(request, "home.html", context)


def expense(request, param):
    client = Client.objects.get(name=param)
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        record = Expense(timestampOfExpense=datetime.now(),
                         clientname=client,
                         amount=form.cleaned_data.get('amount'),
                         currency=form.cleaned_data.get('currency'),
                         title=form.cleaned_data.get('title'),
                         description=form.cleaned_data.get('description')
                         )
        record.save()
        messages.success(request, 'successfully added Expense!')
    queryset = Expense.objects.filter(
        clientname=param).order_by('-timestampOfExpense')
    context = {
        "form": form,
        "queryset": queryset,
        "client": param
    }
    return render(request, "expense.html", context)
