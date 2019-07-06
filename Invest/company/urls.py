from django.urls import path
from . import views


urlpatterns = [
    # Home url 
    path('', views.CompanyView, name='home'),

    # Each Investor Record Url
    path('records/<int:id>/', views.RecordView, name='records'),

    # Total Investment Record
    path('total-record/', views.TotalRecordView, name='total'),
 
    # Total Investment Record
    path('pay/', views.PaymentView, name='payment'),


]
 