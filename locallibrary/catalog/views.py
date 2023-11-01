import datetime

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import RenewBookModelForm
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
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
        'num_roman_books': num_roman_books,
        'num_scifi_genres': num_scifi_genres
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # ваше собственное имя переменной контекста в шаблоне
    queryset = Book.objects.all()  # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'books/book_list.html'  # Определение имени вашего шаблона и его расположения
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'  # ваше собственное имя переменной контекста в шаблоне
    queryset = Author.objects.all()  # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'books/author_list.html'  # Определение имени вашего шаблона и его расположения
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


class AllLoanedBooksListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed.html'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookModelForm(request.POST)

        if form.is_valid():
            book_instance.due_back = form.cleaned_data['due_back']
            book_instance.save()

            return HttpResponseRedirect(reverse('borrowed-books'))

    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookModelForm(initial={'due_back': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/renew_book_librarian.html', context)


class AuthorCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'catalog.add_author'
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}
    permission_denied_message = 'Вы не являетесь администратором для управления авторами'


class AuthorUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'catalog.change_author'
    model = Author
    fields = '__all__'
    permission_denied_message = 'Вы не являетесь администратором для управления авторами'


class AuthorDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'catalog.delete_author'
    model = Author
    success_url = reverse_lazy('books')
    permission_denied_message = 'Вы не являетесь администратором для управления авторами'


class BookCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'catalog.add_book'
    model = Book
    fields = '__all__'
    permission_denied_message = 'Вы не являетесь администратором для управления книгами'


class BookUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'catalog.change_book'
    model = Book
    fields = '__all__'
    permission_denied_message = 'Вы не являетесь администратором для управления книгами'


class BookDelete(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'catalog.delete_book'
    model = Book
    success_url = reverse_lazy('books')
    permission_denied_message = 'Вы не являетесь администратором для управления книгами'
