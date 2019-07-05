from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Investment, Investor


class InvestorsForm(forms.ModelForm):

    class Meta :
        model = Investment
        fields = ['amount', 'rate']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(InvestorsForm, self).__init__(*args, **kwargs)


    # # __init__ is constructor that take parameter when initiated 
    # # you can you this __init__ method to take any parameter when need 
    # def __init__(self, user, *args, **kwargs):
    #     investor = Investment.objects.filter(investor=request.id)
    #     self.user =  investor #Investment.objects.filter(investor=self.request.user.id)
    #     super(InvestorsForm, self).__init__(*args, **kwargs)



    # # def __init__(self, user, *args, **kwargs):
    # #     self.user = user
    # #     super(RSVPForm, self).__init__(*args, **kwargs)




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
