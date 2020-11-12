from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class ProfileView(generic.TemplateView):
    template_name = 'profile.html'