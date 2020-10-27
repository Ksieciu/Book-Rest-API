# Book Rest API
 Recruitment task - Django REST Framework

 Application was created with Django and Django Rest Framework.
 For filtering Django-filters were used.

 Endpoints:
 
 GET /api/books/ - list of all books in database

 GET /api/books/<int:pk> - Detailed info about book with given primary key

 POST /api/db - Endpoing for creating/updating many books at once

 Example json for POST /api/db endpoint:
 https://www.googleapis.com/books/v1/volumes?q=war
