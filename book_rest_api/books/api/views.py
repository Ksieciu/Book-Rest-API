from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..filters import BookFilterSet
from ..models import Book
from .serializers import (DataSerializer, VolumeSerializer, ItemSerializer)


class BooksList(generics.ListAPIView):
    """
    Optionally filters returned books based 
    on a given parameters.
    Also allows for ordering by title, published_date,
    author and category.
    ex. /api/books/?category=Religion&ordering=title
    Use 'filter' button to use simple filter interface.
    """
    queryset = Book.objects.all()
    serializer_class = VolumeSerializer
    filterset_class = BookFilterSet
    ordering_fields = [
        'title',
        'published_date', 
        'author', 
        'category',
    ]


class BookDetails(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = VolumeSerializer


@api_view(['POST'])
def create_update_books_db_view(request, *args, **kwargs):
    """
    View for loading DB from json file via POST.
    Creates book if not exist, else updates.
    """
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({"Database has been updated"}, status=201)
    return Response({}, status=400)


@api_view(['POST'])
def create_book_view(request, *args, **kwargs):
    """
    Made for early testing - creates or updates
    single book.
    Not working at the moment - in order to work
    ItemSerializer needs custom create and
    to_internal_value methods.
    """
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Record created/updated", status=201)
    return Response({}, status=400)