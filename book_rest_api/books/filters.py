from django_filters import rest_framework as filters
from .models import Author, Book, Category


class BookFilterSet(filters.FilterSet):
    """
    Filter for multiple authors and categories. 
    With simple CharFilter it was only possible to make 
    filtering by one author/category at the same time.
    """
    author = filters.ModelMultipleChoiceFilter(
        field_name='author__name',
        to_field_name='name',
        queryset=Author.objects.all()
    )
    category = filters.ModelMultipleChoiceFilter(
        field_name='category__name', 
        to_field_name='name',
        queryset=Category.objects.all(),
    )
    published_date = filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = Book
        fields = [
            'author', 
            'category', 
            'published_date'
        ]