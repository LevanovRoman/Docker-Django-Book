from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .storages import *


class HomeView(TemplateView):
    template_name = "mainapp/index.html"
    context = {'title': 'Главная'}








