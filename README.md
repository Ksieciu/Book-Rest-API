# Book Rest API
 Recruitment task - Django REST Framework

 Application was created with Django and Django Rest Framework.
 For filtering Django-filters were used.

 Endpoints:
 /api/books/ - list of all books in database

 /api/books/<int:pk> - Detailed info about book with given id

 /api/books/db - Endpoing for creating/updating many books at once
 Example json for that endpoing:
 https://www.googleapis.com/books/v1/volumes?q=war
