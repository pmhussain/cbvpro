from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
# Create your views here.
class BookListView(ListView):
    model = Book
    #default template name : book_list.html
    # default context object : book_list
class BookDetailView(DetailView):
    model = Book
    #default template : book_detail.html
    # default context object : book


#for creating and upadting data we need to write form class in forms.py
class BookCreateView(CreateView):
    model = Book
    fields = ('title', 'author', 'pages', 'price')

class BookUpdateView(UpdateView):
    model = Book
    fields = ('title', 'author', 'pages', 'price')

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('bookslist')
