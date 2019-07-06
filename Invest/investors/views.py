from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import UserRegistrationForm, InvestorsForm

from django.views.generic import ListView
from django.http import HttpResponse


# Form that allow logged in user to invest 
def InvestView(request):
    if request.method == 'GET':
        investment_form = InvestorsForm(request.user)
        context = {'investment_form': investment_form}
        return render(request, 'investors/form.html', context)
    if request.method == 'POST':
        investment_form = InvestorsForm(request.POST or None, instance=request.user)

        if investment_form.is_valid():
            amount = investment_form.cleaned_data['amount']
            interest = investment_form.cleaned_data['rate']
            saving = investment_form.save(commit=False)
            investor = request.user
            print(investor)
            saving.investor = investor
            # Passing Logged in user
            # investor = request.user
            # print(investor)
            # saving.investor.user = request.user
            saving.save()
            messages.success(request, f'New Investment Done!')
            return render(request, 'investor/myinvest.html')    

# class based views
#List where user can see the record of their past investment
# class InvestmentListView(ListView):
#     model = Investment
#     template_name = 'investors/myinvest.html'
#     context_object_name = 'total_invested_by_user'


#     def get_queryset(self):
#         return  Investment.objects.filter(investor=self.request.user.id)



@login_required
def InvestmentListView(request):
    investors = Investment.objects.filter(investor__user=request.user)
    print(investors)
    args = {'investors':investors}
    return render(request, 'investors/myinvest.html', args)


# Register 
def RegisterView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            print("New User Account created -", username)
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else: # else is used if request is not post then run else part 
        form = UserRegistrationForm()
    return render(request, 'investors/register.html', {'form': form})


