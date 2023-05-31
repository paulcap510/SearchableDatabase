# Generated by Django 4.2.1 on 2023-05-30 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author_affiliation', models.CharField(max_length=200)),
                ('author_geography', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author_affiliation', models.CharField(max_length=200)),
                ('author_geography', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OtherPublication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
                ('vol', models.PositiveIntegerField()),
                ('issue', models.PositiveIntegerField()),
                ('topic_geography', models.CharField(max_length=200)),
                ('authors', models.ManyToManyField(to='myapp.author')),
            ],
        ),
        migrations.CreateModel(
            name='Manuscript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
                ('vol', models.PositiveIntegerField()),
                ('issue', models.PositiveIntegerField()),
                ('topic_geography', models.CharField(max_length=200)),
                ('authors', models.ManyToManyField(to='myapp.author')),
            ],
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
                ('vol', models.PositiveIntegerField()),
                ('issue', models.PositiveIntegerField()),
                ('topic_geography', models.CharField(max_length=200)),
                ('book_author', models.ManyToManyField(to='myapp.bookauthor')),
                ('book_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.book')),
                ('reviewers', models.ManyToManyField(to='myapp.author')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='myapp.bookauthor'),
        ),
    ]