# Generated by Django 3.0.7 on 2024-11-25 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='ingredients',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='making_time',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='serves',
            field=models.CharField(max_length=50, null=True),
        ),
    ]