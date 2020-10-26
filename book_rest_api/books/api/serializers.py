from rest_framework import serializers
from ..models import Author, Book, Category


class ThumbnailSerializer(serializers.Serializer):
    '''
    Serializer for grabbing thumbnail from nested
    imageLinks 
    '''
    thumbnail = serializers.URLField()


class VolumeSerializer(serializers.ModelSerializer):
    '''
    Serializer for Book model. Takes all fields
    except volume_id
    '''
    authors = serializers.SlugRelatedField(
        source='author', 
        many=True, 
        slug_field='name', 
        queryset=Author.objects.all()
    )
    categories = serializers.SlugRelatedField(
        source='category', 
        many=True, 
        required=False,
        slug_field='name', 
        queryset=Category.objects.all()
    )
    publishedDate = serializers.CharField(
        source='published_date', 
        required=False
    )
    pageCount = serializers.IntegerField(
        source='page_count', 
        required=False
    )
    averageRating = serializers.DecimalField(
        source='average_rating',
        max_digits=2,
        decimal_places=1,
        required=False
    )
    ratingsCount = serializers.IntegerField(
        source='ratings_count', 
        required=False
    )
    imageLinks = ThumbnailSerializer(required=False)

    class Meta:
        model = Book
        fields = [
            "title", 
            "authors", 
            "publishedDate", 
            "pageCount", 
            "categories", 
            "averageRating", 
            "ratingsCount",
            "imageLinks",]


class ItemSerializer(serializers.Serializer):
    '''
    Serializer for getting volume_id and 
    nested volumeInfo
    '''
    id = serializers.CharField(source="volume_id")
    volumeInfo = VolumeSerializer(many=False, write_only=True)


class DataSerializer(serializers.Serializer):
    '''
    Serializer for saving items
    (with nested id and books) to db.
    '''
    items = ItemSerializer(many=True, write_only=True)

    def to_internal_value(self, validated_data):
        '''
        get authors and categories nested in volumeInfo 
        and check if exist in db. If not, then create 
        new Author/Category.
        '''
        for item in validated_data['items']:
            authors_data = item['volumeInfo'].get('authors', None)
            categories_data = item['volumeInfo'].get('categories', None)
            if authors_data:
                for author_name in authors_data:
                    author = Author.objects.get_or_create(name=author_name)
            if categories_data:
                for category_name in categories_data:
                    category = Category.objects.get_or_create(name=category_name)
        return super().to_internal_value(validated_data)

    def create(self, validated_data):
        """
        Iterate through items(books) data and create new 
        book if book with given volume_id not exist in db. 
        Otherwise update book. Then clear all book object
        relations and add relations to categories and
        authors given in validated_data. 
        """
        for item in validated_data['items']:
            volume_data = item['volumeInfo']
            authors_data = volume_data.pop('author', None)
            categories_data = volume_data.pop('category', None)
            imageLinks_data = volume_data.pop('imageLinks', None)
            
            if imageLinks_data:
                book, created = Book.objects.update_or_create(
                    volume_id=item['volume_id'],
                    defaults={
                        **volume_data, 
                        'thumbnail': imageLinks_data["thumbnail"]
                    }
                )
            else:
                book, created = Book.objects.update_or_create(
                    volume_id=item['volume_id'],
                    defaults={**volume_data}
                )
            book.author.clear()
            book.category.clear()
            if authors_data:
                for author in authors_data:
                    book.author.add(author)
            if categories_data:
                for category in categories_data:
                    book.category.add(category)
        return book