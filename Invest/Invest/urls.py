from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views   # Class-bassed Views
from investors import views as user_views

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('company.urls')),
    path('', include('investors.urls')),

    # Login and Logout Url
    path('login/', auth_views.LoginView.as_view(template_name='investors/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='investors/logout.html'), name='logout'),

]
