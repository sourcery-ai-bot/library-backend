# Generated by Django 2.2.1 on 2019-05-27 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libbackend', '0005_auto_20190407_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookimage',
            options={'verbose_name': 'Book image', 'verbose_name_plural': 'Book images'},
        ),
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookimage',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='book_image', to='libbackend.Book'),
        ),
        migrations.CreateModel(
            name='Book2User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_link_type', models.CharField(choices=[('own', 'Owner'), ('obs', 'Observer'), ('bor', 'Borrower')], default='own', max_length=3)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libbackend.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Book to user',
                'verbose_name_plural': 'Books to users',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='books', through='libbackend.Book2User', to=settings.AUTH_USER_MODEL),
        ),
    ]