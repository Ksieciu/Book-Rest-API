from django.urls import path
from .views import (
    BooksList, 
    BookDetails, 
    create_update_books_db_view, 
    # create_book_view
)


urlpatterns = [
    path('books/', BooksList.as_view()),
    path('books/<int:pk>', BookDetails.as_view()),
    path('db/', create_update_books_db_view),
    # path('books/create', create_book_view),
]
