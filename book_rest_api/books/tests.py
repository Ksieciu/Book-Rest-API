import os
import json
from django.test import TestCase
from rest_framework.test import APIClient


def read_file_data(filename):
    with open(filename, encoding="utf8") as data_file:
        json_data = json.load(data_file)
    return json_data


class TestBooksAPI(TestCase):

    def get_client(self):
        client = APIClient()
        return client

    def test_load_json_db(self):
        client = self.get_client()
        data = read_file_data('volumes.json')
        response = client.post('/api/books/db', data=data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 200)