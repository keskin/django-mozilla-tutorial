from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    path('author/create', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete', views.AuthorDelete.as_view(), name='author-delete'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('all-books/', views.LoanedBooksLibrarianListView.as_view(), name='all-books'),
    path('book/<uuid:pk>/renew', views.renew_book_librarian, name='renew-book-librarian'),
]