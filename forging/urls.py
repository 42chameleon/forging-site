from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:category_id>/', ForgingByCategory.as_view(), name='category'),
]