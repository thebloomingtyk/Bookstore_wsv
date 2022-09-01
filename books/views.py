from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
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


class SearchResultsListView(ListView):
    model = models.Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    queryset = models.Book.objects.filter(title__icontains='beginners')

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return models.Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    )