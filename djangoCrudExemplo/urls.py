"""djangoCrudExemplo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from crudapp import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("crudapp.urls")),
    path("api/", include("crudapp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('contacts/', views.IndexView.as_view(), name='index'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
    path('contacts/edit/<int:pk>/', views.edit, name='edit'),
    path('contacts/create/', views.create, name='create'),
    path('contacts/delete/<int:pk>/', views.delete, name='delete'),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]
