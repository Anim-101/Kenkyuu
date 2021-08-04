from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('api/data/insert', DataInsertView.as_view(), name="insert_data")
]