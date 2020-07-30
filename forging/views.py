from django.shortcuts import render
from django.views.generic import ListView
from .models import Forging, Category


class HomeView(ListView):
    model = Forging
    template_name = 'forging/home_forging_list.html'
    context_object_name = 'forging'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Forging.objects.filter(is_published=True).select_related('category')
