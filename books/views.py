from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.all()
    years = Book.objects.dates('pub_date', 'year', order='DESC')
    context = {'books_objects': books_objects, 'years': years}
    return render(request, template, context)


def books_by_year_view(request, year):
    template = 'books/books_list.html'
    books_objects = Book.objects.filter(pub_date__year=year)
    years = Book.objects.dates('pub_date', 'year', order='DESC')
    context = {'books_objects': books_objects, 'years': years, 'current_year': year}
    return render(request, template, context)


def book_detail_view(request, book_id):
    template = 'books/book_detail.html'
    book = get_object_or_404(Book, id=book_id)
    years = Book.objects.dates('pub_date', 'year', order='DESC')
    context = {'book': book, 'years': years}
    return render(request, template, context)
