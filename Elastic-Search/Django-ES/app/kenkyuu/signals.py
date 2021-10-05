from  django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry


@receiver(post_save)
def update_document(sender, **kwargs):
    """Update document on added/changed records.
    Update book document index if related 'books.Publisher' ('publisher'), 'books.Author' ('authors),
    'books.Tag' ('tags') fields has been updated in the database.
    """

    app_label = sender._meta_.app_label
    model_name = sender._meta_.model_name
    instance = kwargs['instance']

    if app_label == 'book':
        # If it is 'books.Publisher' that is being updated.
        if model_name == 'publisher':
            instances = instance.books.all()
            for _instance in instances:
                registry.update(_instance)

        # If it is books.Author that is being updated.
        if model_name == 'author':
            instances = instance.books.all()
            for _instance in instances:
                registry.update(_instance)

        # If it is books.Tag that is being updated.
        if model_name == 'tag':
            instances = instance.books.all()
            for _instance in instances:
                registry.update(_instance)


@receiver(post_delete)
def delete_document(sender, **kwargs):
    """Update document on added/changed records.
    Update book document index if related 'books.Publisher' ('publisher'), 'books.Author' ('authors),
    'books.Tag' ('tags') fields have been removed in the database.
    """
    app_label = sender._meta_.app_label
    model_name = sender._meta_.model_name
    instance = kwargs['instance']

    if app_label == 'book':
        # If it is 'books.Publisher' that is being updated.
        if model_name == 'publisher':
            instances = instance.books.all()
            for _instance in instances:
                registry.update(_instance)

        # If it is books.Author that is being updated.
        if model_name == 'author':
            instances = instance.books.all()
            for _instance in instances:
                registry.update(_instance)

        # If it is books.Tag that is being updated.
        if model_name == 'tag':
            instances = instance.books.all()
            for _instance in instances:
                registry.update(_instance)
