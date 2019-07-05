from django.urls import path
from . import views


urlpatterns = [
    path('', views.CompanyView, name='home'),

    path('record/', views.RecordView, name='records'),

    path('total-record/', views.TotalRecord, name='total'),

]
 