from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('api/data/insert', DataInsertView.as_view(), name="insert_data"),
    path('api/data/fetch', DataFetchView.as_view(), name="search_data"),
    path('api/data/fetch/chunk/', DataFetchChunkView.as_view(), name="fetch_chunk_data")
]