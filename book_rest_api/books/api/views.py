from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Book
from .serializers import DataSerializer, VolumeSerializer, ItemSerializer


class BooksList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = VolumeSerializer
    filterset_fields = [
        'published_date', 
        'author__name', 
        'category',
    ]
    ordering_fields = [
        'title',
        'published_date', 
        'author', 
        'category',
    ]

    """
    Optionally filters returned books based 
    on a given author or date queryset parameters.
    ex. /api/books/?category=Religion
    Also allows for ordering by publishedDate and 
    author if `?ordering=` is added to url.
    """


class BookDetails(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = VolumeSerializer


@api_view(['POST'])
def create_update_books_db_view(request, *args, **kwargs):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(['POST'])
def create_book_view(request, *args, **kwargs):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)