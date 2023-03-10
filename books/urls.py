from django.urls import path
from .views import ListViewBook

urlpatterns = [
    path('', ListViewBook.as_view(), name='home')
]