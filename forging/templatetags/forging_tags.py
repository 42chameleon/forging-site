from django import template
from forging.models import Category
from django.db.models import Count

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('forging/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}