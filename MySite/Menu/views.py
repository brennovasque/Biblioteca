from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .forms import AddBook, AddGenre, AddAuthor
from .models import Book, Genre


def index(request):
    context = {
        'texto': 'a'
    }
    return render(request, 'landing_page/index.html', context=context)


class BookList(ListView):
    model = Book
    template_name = 'landing_page/tabela_livros.html'


class CreateBook(CreateView):
    model = Book
    template_name = 'landing_page/add_edit_livro.html'
    form_class = AddBook
    extra_context = {
        'titulo': 'Adicione um Livro à Biblioteca! 📚',
        'botao': 'Adicionar Livro'
    }

    def get_success_url(self):
        return reverse_lazy('list')


class DeleteBook(DeleteView):
    model = Book
    template_name = 'landing_page/remover_livro.html'

    def get_success_url(self):
        return reverse_lazy('list')


class EditBook(UpdateView):
    model = Book
    form_class = AddBook
    template_name = 'landing_page/add_edit_livro.html'
    extra_context = {
        'titulo': 'Edite o Livro',
        'botao': 'Editar Livro'
    }

    def get_success_url(self):
        return reverse_lazy('list')


class CreateGenre(CreateView):
    model = Genre
    form_class = AddGenre
    template_name = 'landing_page/create-item.html'
    extra_context = {
        'titulo': 'Crie um Gênero',
        'botao': 'Criar'
    }

    def get_success_url(self):
        return reverse_lazy('create')


class CreateAuthor(CreateView):
    model = Genre
    form_class = AddAuthor
    template_name = 'landing_page/create-item.html'
    extra_context = {
        'titulo': 'Crie um Autor',
        'botao': 'Criar'
    }

    def get_success_url(self):
        return reverse_lazy('create')
