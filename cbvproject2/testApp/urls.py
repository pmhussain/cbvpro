from django.urls import path
from . import views
urlpatterns = [
    path('', views.BookListView.as_view(), name='bookslist'),
    path('create', views.BookCreateView.as_view()),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name = 'bookdetail'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name = 'bookdupdate'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name = 'bookdelete'),
]
