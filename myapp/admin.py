from django.contrib import admin
from .models import Admin
from .models import Author, Book, BookAuthor, Manuscript, BookReview, OtherPublication

admin.site.register(Admin)
admin.site.register(Author)

admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(Manuscript)
admin.site.register(BookReview)
admin.site.register(OtherPublication)