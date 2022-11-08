from django.urls import path, include
from . import views

from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('welcome', views.welcome),
    path('obtercontatos', views.obter_contatos),
]
