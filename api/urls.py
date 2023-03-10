from django.urls import path
from .views import BookAPIView
from books.views import ListViewBook

urlpatterns = [
    path('', BookAPIView.as_view())
]