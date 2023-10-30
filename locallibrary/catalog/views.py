from django.shortcuts import render
from django.views import generic

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


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # ваше собственное имя переменной контекста в шаблоне
    queryset = Book.objects.all() # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'books/book_list.html'  # Определение имени вашего шаблона и его расположения
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'   # ваше собственное имя переменной контекста в шаблоне
    queryset = Author.objects.all() # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'books/author_list.html'  # Определение имени вашего шаблона и его расположения
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
