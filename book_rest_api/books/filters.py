from django_filters import rest_framework as filters
from .models import (Author, Book, Category)



class BookFilterSet(filters.FilterSet):
    author = filters.ModelMultipleChoiceFilter(
        field_name='author__name',
        lookup_expr='icontains',
        queryset=Author.objects.all())
    category = filters.ModelMultipleChoiceFilter(field_name='category__name', queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = ['author', 'category', 'published_date']

    def filter_author(self, queryset, name, value):
        return 