from django.db import models
from django.conf import settings
from django.utils.translation import gettext, gettext_lazy as _
import json

# Status of the book
BOOK_PUBLISHING_STATUS_PUBLISHED = 'published'
BOOK_PUBLISHING_STATUS_NOT_PUBLISHED = 'not_published'
BOOK_PUBLISHING_STATUS_IN_PROGRESS = 'in_progress'
BOOK_PUBLISHING_STATUS_CANCELLED = 'cancelled'
BOOK_PUBLISHING_STATUS_REJECTED = 'rejected'
BOOK_PUBLISHING_STATUS_CHOICES = (
    (BOOK_PUBLISHING_STATUS_PUBLISHED, 'Published'),
    (BOOK_PUBLISHING_STATUS_NOT_PUBLISHED, 'Not published'),
    (BOOK_PUBLISHING_STATUS_IN_PROGRESS, 'In Progress'),
    (BOOK_PUBLISHING_STATUS_CANCELLED, 'Cancelled'),
    (BOOK_PUBLISHING_STATUS_REJECTED, 'rejected'),
)
BOOK_PUBLISHING_STATUS_DEFAULT = BOOK_PUBLISHING_STATUS_PUBLISHED

class Publisher(models.Model):
    """Publisher Model"""

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=69)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()
    latitude = models.DecimalField(null=True,
                                   blank=True,
                                   decimal_places=15,
                                   max_digits=19,
                                   default=0)
    longitude = models.DecimalField(null=True,
                                   blank=True,
                                   decimal_places=15,
                                   max_digits=19,
                                   default=0)

    class Meta:
        """Meta Options"""

        ordering = ["id"]

    def __str__(self):
        return self.name

    def location_field_iondexing(self):
        """Location for indexing,
        User in Elasticsearch indexing/tests of 'geo_distance' native filter,
        """
        return {
            'lat': self.latitude,
            'lon': self.longitude,
        }

class Author(models.Model):
    """Author Model"""

    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='authors', null=True, blank=True)

    class Meta:
        """Meta Options"""

        ordering = ["id"]

    def __str__(self):
        return self.name

class Tag(models.Model):
    """Tag Model"""

    title = models.CharField(max_length=255, unique=True)

    class Meta:
        """Meta Options"""

        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.title

class Book(models.Model):
    """Book Model"""

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField()
    state = models.CharField(max_length=100,
                             choices=BOOK_PUBLISHING_STATUS_CHOICES,
                             default=BOOK_PUBLISHING_STATUS_DEFAULT)
    isbn = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.PositiveIntegerField(default=200)
    stock_count = models.PositiveIntegerField(default=30)
    tags = models.ManyToManyField(Tag, related_name='books', blank=True)

    class Meta:
        """Meta Options"""

        ordering = ['isbn']

    def __str__(self):
        return self.title

    @property
    def publisher_indexing(self):
        """Publisher for indexing
        User in Elasticsearch
        """

        if self.publisher is not None:
            return self.publisher.name

    @property
    def tags_indexing(self):
        """Tags for indexing,
        Used in Elasticsearch indexing.
        """
        return [tag.title for tag in self.tags.all()]


