"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from users.views import (
    registration_view,
    logout_view,
    login_view,
    remove_user_view,
    account_view
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    # path('users/', include('users.api.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('registration/', registration_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),
    path('delete_account/', remove_user_view, name='delete_account'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name='registration/password_change.html'),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
