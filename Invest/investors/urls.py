from django.urls import path
from . import views

from investors import views as user_views


urlpatterns = [
    path('myinvest/', views.InvestmentDetailView, name='myinvest'),
    path('register/', user_views.RegisterView, name='register'),

]
