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
        self.book = Book.objects.create(
            volume_id='ABC',
            title = 'Test Title',
            published_date = '2020',
            page_count = 123,
            average_rating = 3.0,
            ratings_count = 10
        )
        self.book.author.add(self.author)
        self.book.category.add(self.category)

    def get_client(self):
        client = APIClient()
        return client

    def test_load_json_db(self):
        '''
        check if data from json file loaded to db
        with 201 success status code and check if 
        len of books list(all books in db) is 11.
        '''
        client = self.get_client()
        data = read_file_data('test_data/volumes.json')
        response = client.post('/api/books/db', data=data, format='json')
        self.assertEqual(response.status_code, 201)
        response = client.get('/api/books/')
        self.assertEqual(len(response.data), 11)

    def test_show_book_details(self):
        client = self.get_client()
        response = client.get('/api/books/1')
        title = "Test Title"
        self.assertEqual(response.data['title'], title)

    def test_change_categories(self):
        '''
        Read file that has changed categories in first book
        placed earlier in db, then GET that book info from 
        db and check if changed categories are equal to 
        categories data from file.
        '''
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

    # def test_change_no_category(self):
    #     client = self.get_client()
    #     data = read_file_data('test_data/change_no_category.json')
    #     response = client.post('/api/books/db', data=data, format='json')
    #     print(response.data)
    #     self.assertEqual(response.status_code, 201)

    