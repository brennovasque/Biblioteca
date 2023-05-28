from django.urls import path, include
from .views import BookList, CreateBook, DeleteBook, EditBook, CreateGenre, CreateAuthor

# API
from .api import viewsets as booksviewset
from rest_framework import routers

route = routers.DefaultRouter()

route.register(r'books', booksviewset.BooksViewSet, basename='Books')

urlpatterns = [
    path('list/', BookList.as_view(), name='list'),
    path('create/', CreateBook.as_view(), name='create'),
    path('remove/<pk>', DeleteBook.as_view(), name='remove'),
    path('edit/<pk>', EditBook.as_view(), name='edit'),
    path('create-genre/', CreateGenre.as_view(), name='create-genre'),
    path('create-author/', CreateAuthor.as_view(), name='create-author'),
    path('', include(route.urls))

]
