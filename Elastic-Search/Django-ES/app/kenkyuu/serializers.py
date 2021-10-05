import json
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .elasticsearch import BookDocument


class BookDocumentSerializer(DocumentSerializer):
    """Serializer for the book document."""

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    summary = serializers.CharField(read_only=True)
    publisher = serializers.CharField(read_only=True)
    publication_date = serializers.DateField(read_only=True)
    state = serializers.CharField(read_only=True)
    isbn = serializers.CharField(read_only=True)
    price = serializers.CharField(read_only=True)
    pages = serializers.IntegerField(read_only=True)
    stock_count = serializers.IntegerField(read_only=True)
    tags = serializers.SerializerMethodField()

    class Meta:
        """Meta optioons."""

        # Specifying correspondent document class
        document = BookDocument

        # List the serializer fields, note that the order of the fields is
        # preserved in the viewset.
        fields = {
            'id',
            'title',
            'description',
            'summary',
            'publisher',
            'publication_date',
            'state',
            'isbn',
            'price',
            'pages',
            'stock_count',
            'tags',
        }