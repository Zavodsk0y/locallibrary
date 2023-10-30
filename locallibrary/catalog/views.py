from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.
    num_roman_books = Book.objects.filter(title__icontains='нашего').count()
    num_scifi_genres = Genre.objects.filter(name__icontains='Фантастика').count()




    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_roman_books': num_roman_books, 'num_scifi_genres': num_scifi_genres},
    )
