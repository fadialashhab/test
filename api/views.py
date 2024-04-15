from django.shortcuts import render
from rest_framework import generics
from books.models import Books
from .serializer import BookSerializer
# Create your views here.

class BookApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer