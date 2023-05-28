from rest_framework import viewsets
from . import serializers
from .. import models


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Book.objects.all()
