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
    try:
        investor = Investor.objects.get(user=request.user)
        print(investor)
        name = investor.name 
        print(name)
        amount = int(request.POST.get('amount'))
        rate = int(request.POST.get('rate'))

        return redirect(request, 'investors/myinvest.html')
    except:
        pass

    return render(request, 'investors/form.html')
    







        # else:
        #     investment_form = InvestorsForm(request.user)
        #     args = {'investment_form': investment_form}
        #     return render(request, 'investors/form.html', args)



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


