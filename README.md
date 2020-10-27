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

 /api/books/create - Endpoint for creating single book
 Example json:
 
 {
    "title": "Hobbit czyli Tam i z powrotem",
    "authors": [
      "J. R. R. Tolkien"
    ],
    "publishedDate": "2004",
    "pageCount": 315,
    "categories": [
      "Baggins, Bilbo (Fictitious character)"
    ],
    "averageRating": 5,
    "ratingsCount": 2,
    "imageLinks": {
      "smallThumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
      "thumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
    }
  }

