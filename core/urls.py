from django.urls import path
from .views import HomeView, ItemDetailView, checkout;


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]