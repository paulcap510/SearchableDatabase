from django.shortcuts import render
from django.db.models import Q

from .models import Manuscript, BookReview, OtherPublication


def admin_login(request):
    return render(request, 'myapp/admin_login.html')

def index(request):
    query = request.GET.get('q')
    manuscripts = Manuscript.objects.filter(
        Q(title__icontains=query) |
        Q(authors__name__icontains=query) |
        Q(topic_geography__icontains=query) |
        Q(authors__author_affiliation__icontains=query)
    ) if query else []
    book_reviews = BookReview.objects.filter(
        Q(book_title__title__icontains=query) |
        Q(reviewers__name__icontains=query) |
        Q(topic_geography__icontains=query) |
        Q(book_author__name__icontains=query) |
        Q(book_author__author_affiliation__icontains=query)
    ) if query else []
    other_publications = OtherPublication.objects.filter(
        Q(title__icontains=query) |
        Q(authors__name__icontains=query) |
        Q(topic_geography__icontains=query) |
        Q(authors__author_affiliation__icontains=query)
    ) if query else []
    context = {
        'manuscripts': manuscripts,
        'book_reviews': book_reviews,
        'other_publications': other_publications,
    }
    return render(request, 'myapp/index.html', context=context)