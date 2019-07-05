from django.urls import path
from . import views

from investors import views as user_views




urlpatterns = [
    path('myinvest/', views.InvestmentListView, name='myinvest'),

    #path('myinvest/', views.InvestmentListView, name='myinvest'),
    
    path('register/', user_views.RegisterView, name='register'),

    #path('invest/new/', PostInvestView.as_view(), name="invest"),

    path('invest/', views.InvestView, name='invest'),


    

]
