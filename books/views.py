from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books import models


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = models.Book
    context_object_name = 'book_list'
    template_name = 'book/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Book
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'
