from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import DataSerializer, VolumeSerializer


class BooksList(generics.ListAPIView):
    serializer_class = VolumeSerializer

    def get_queryset(self):
        """
        Optionally filters the returned books based 
        on a given author or date queryset parameters.

        Also allows for ordering by publishedDate and 
        author if `?ordering=` is added to url.
        
        """
        queryset = Book.objects.all()
        # filter_backends = [DjangoFilterBackend]
        filterset_fields = ['publishedDate', 'author']
        ordering_fields = ['publishedDate', 'author']
        return queryset


@api_view(['POST', 'PUT'])
def create_update_books_db_view(request, *args, **kwargs):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(['POST', 'PUT'])
def create_book_view(request, *args, **kwargs):
    serializer = VolumeSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)