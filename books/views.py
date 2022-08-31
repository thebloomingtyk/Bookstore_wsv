from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books import models


# Create your views here.
class BookListView(ListView):
    model = models.Book
    context_object_name = 'book_list'
    template_name = 'book/book_list.html'


class BookDetailView(DetailView):
    model = models.Book
    template_name = 'books/book_detail.html'
