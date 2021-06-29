from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """View handling the home page of the website."""
    template_name = "pages/home.html"