from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.

class BooksView(ListView):
    model = models.Books
    template_name = 'books.html'
    context_object_name = 'books'