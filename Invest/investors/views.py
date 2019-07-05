from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import UserRegistrationForm, InvestorsForm

from django.views.generic import ListView



def InvestView(request):
    if request.method == 'POST':
        form = InvestorsForm(request.POST or None, instance=request.user)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            rate = form.cleaned_data['rate']
            instance = form.save(commit=False)
            instance.name = request.user.id
            print(instance.name)
            instance.save()
            return redirect('myinvest')
    else:
        form = InvestorsForm()
        args = {'form':form}
    return render(request, 'investors/form.html', args)




class InvestmentListView(ListView):
    model = Investment
    template_name = 'investors/myinvest.html'
    context_object_name = 'total_invested_by_user'


    def get_queryset(self):
        return  Investment.objects.filter(investor=self.request.user.id)







# class InvestmentListView(ListView):
#     model = Investment
#     template_name = 'investors/myinvest.html'
#     context_object_name = 'total_invested_by_user'


#     def get_queryset(self):
#         return  Investment.objects.filter(investor=self.request.user)



# def InvestmentDetailView(request):

#     return render(request, 'investors/myinvest.html')




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


