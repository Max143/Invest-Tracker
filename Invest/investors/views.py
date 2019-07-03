from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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



def InvestmentDetailView(request):
    return render(request, 'investors/myinvest.html')