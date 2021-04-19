# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from p_library.models import Book, Publisher, Reader
#from django.core import serializers

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    books_count = books.count()
    biblio_data = {
        "title": "мою библиотеку",
        "books_count": books_count,
        "books": books,
    }
    return HttpResponse(template.render(biblio_data))

def pub_list(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.all()
    books = Book.objects.all()
    pub_data = {
        "publishers": publishers,
        "books": books,
    }
    return HttpResponse(template.render(pub_data))

def reader_list(request):
    template = loader.get_template('readers.html')
    readers = Reader.objects.all()
    books = Book.objects.all()
    read_data = {
        "readers": readers,
        "books": books,
    }
    return HttpResponse(template.render(read_data))
