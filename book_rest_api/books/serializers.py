from rest_framework import serializers
from .models import Author, Book, Category


class ThumbnailSerializer(serializers.Serializer):
    thumbnail = serializers.URLField()


class VolumeSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    publishedDate = serializers.CharField(
        source='published_date', 
        required=False
    )
    pageCount = serializers.IntegerField(
        source='page_count', 
        required=False
    )
    categories = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    averageRating = serializers.DecimalField(
        source='average_rating',
        max_digits=3,
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

    def create(self, validated_data):
        # authors_data = validated_data.pop('authors')
        # categories_data = validated_data.pop('categories')
        imageLinks_data = validated_data.pop('imageLinks')
        print('1boop')
        book = Book.objects.create(
            **validated_data, 
            thumbnail=imageLinks_data["thumbnail"]
        )
        # print('2boop')
        # for author_name in authors_data:
        #     author_qs = Author.objects.all()
        #     if Author.objects.filter(name=author_name).exists():
        #         author = Author.objects.filter(name=author_name)
        #     else:
        #         author = Author.objects.create(name=author_name)
        # #     book.author.add(author)
        # print('3boop')
        # for category_name in categories_data:
        #     category_qs = Category.objects.all()
        #     if category_name not in category_qs.values_list('name'):
        #         category = Category.objects.create(name=category_name)
        #     else:
        #         category = Category.objects.filter(name=category_name)
        #     book.categories.add(category)

        # choice_set_serializer = self.fields['choice_set']
        print('4boop')
        return book


class ItemSerializer(serializers.Serializer):
    # kind = serializers.CharField(max_length=200)
    # id = serializers.CharField()
    # etag = serializers.CharField(max_length=200)
    # selfLink = serializers.URLField(max_length=200, min_length=None, allow_blank=False)
    volumeInfo = VolumeSerializer(many=False)


class DataSerializer(serializers.Serializer):
    # kind = serializers.CharField()
    # totalItems = serializers.IntegerField()
    items = ItemSerializer(many=True)