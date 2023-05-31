from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class BookAuthor(models.Model):
    name = models.CharField(max_length=200)
    author_affiliation = models.CharField(max_length=200)
    author_geography = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    author_affiliation = models.CharField(max_length=200)
    author_geography = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(BookAuthor)

    def __str__(self):
        return self.title

class Manuscript(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    keywords = models.CharField(max_length=200)
    vol = models.PositiveIntegerField()
    issue = models.PositiveIntegerField()
    topic_geography = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class BookReview(models.Model):
    book_title = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewers = models.ManyToManyField(Author)
    book_author = models.ManyToManyField(BookAuthor)
    publisher = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    vol = models.PositiveIntegerField()
    issue = models.PositiveIntegerField()
    topic_geography = models.CharField(max_length=200)

    def __str__(self):
        return self.book_title

class OtherPublication(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    type = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    vol = models.PositiveIntegerField()
    issue = models.PositiveIntegerField()
    topic_geography = models.CharField(max_length=200)

    def __str__(self):
        return self.title