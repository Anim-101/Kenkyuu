from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
books = router.register(r'books', BookDocumentView, basename='bookdocument')

urlpatterns = [
    path('api', include(router.urls), name='api'),
    path('api/kenkyu/books/', BookDocumentView, name='bookdocument'),
]