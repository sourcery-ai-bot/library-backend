# Generated by Django 2.1.4 on 2019-01-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libbackend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isbn',
            new_name='isbn10',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='pagecount',
            new_name='page_count',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publishedDate',
            new_name='published_date',
        ),
        migrations.AddField(
            model_name='book',
            name='isbn13',
            field=models.CharField(default=5, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]