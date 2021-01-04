import os
import json
from django.test import TestCase
from rest_framework.test import APIClient
from .models import (Author, Book, Category)


def read_file_data(filename):
    with open(filename, encoding="utf8") as data_file:
        json_data = json.load(data_file)
    return json_data


class TestBooksAPI(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.category = Category.objects.create(name="Test")
        self.author2 = Author.objects.create(name="Second Test Author")
        self.category2 = Category.objects.create(name="Second Test")
        self.book = Book.objects.create(
            volume_id="ABC",
            title = "Test Title",
            published_date = "2020",
            page_count = 123,
            average_rating = 3.0,
            ratings_count = 10
        )
        self.book2 = Book.objects.create(
            volume_id="EFG",
            title = "Second Title",
            published_date = "1999-10-20",
            page_count = 234,
            average_rating = 4.0,
            ratings_count = 6
        )
        self.book.author.add(self.author)
        self.book.category.add(self.category)
        self.book2.author.add(self.author2)
        self.book2.category.add(self.category2)

    def get_client(self):
        client = APIClient()
        return client

    def test_load_json_db(self):
        """
        check if data from json file loaded to db
        with 201 success status code and check if 
        len of books list(all books in db) is 12.
        """
        client = self.get_client()
        data = read_file_data('test_data/volumes.json')
        response = client.post('/api/books/db', data=data, format='json')
        self.assertEqual(response.status_code, 201)
        response = client.get('/api/books/')
        self.assertEqual(len(response.data), 12)

    def test_show_book_details(self):
        client = self.get_client()
        response = client.get('/api/books/1')
        title = "Test Title"
        self.assertEqual(response.data['title'], title)

    def test_show_by_ordering(self):
        """
        Order by ascending published date and check
        if ordered correctly by looking at first result date
        """
        client = self.get_client()
        response = client.get('/api/books/?ordering=published_date')
        oldest_book_date = "1999-10-20"
        self.assertEqual(
            response.data[0]['publishedDate'], 
            oldest_book_date
        )
    
    def test_show_filtered(self):
        """
        Filter GET result to get one author and check
        if filtered result's title is correct and
        response.data number is one
        """
        client = self.get_client()
        response = client.get('/api/books/?author=Second+Test+Author')
        title = "Second Title"
        self.assertEqual(response.data[0]['title'], title)
        self.assertEqual(len(response.data), 1)

    def test_change_categories(self):
        """
        Read file that has changed categories in first book
        placed earlier in db, then GET that book info from 
        db and check if changed categories are equal to 
        categories data from file.
        """
        client = self.get_client()
        data = read_file_data('test_data/change_categories.json')
        response = client.post('/api/books/db', data=data, format='json')
        self.assertEqual(response.status_code, 201)
        response = client.get('/api/books/1')
        categories = [
            "Testing Change Category 1", 
            "Testing Change Category 2"
        ]
        self.assertEqual(response.data['categories'], categories)

 
    