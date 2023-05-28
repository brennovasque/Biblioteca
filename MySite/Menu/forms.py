
from django import forms
from .models import Book, Genre, Author


class AddBook(forms.ModelForm): #Tela_de_Adicionar_Livros

    class Meta:
        model = Book
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Nome'}),
            'genre':  forms.Select(attrs={'class': "form-control"}),
            'author': forms.Select(attrs={'class': "form-control"}),
            'amountPages': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Quantidade de Páginas'}),
            'publicationDate': forms.DateInput(format='%d/%m/%Y', attrs={'class': "form-control"}),
            'rent': forms.CheckboxInput()
        }

        labels = {
            'name': "Nome",
            'genre': "Gênero",
            'author': "Autor",
            'amountPages': "Quantidade de Páginas",
            'publicationDate': "Data da Publicação",
            'rent': "Alugado?"
        }


class AddGenre(forms.ModelForm):

    class Meta:
        model = Genre
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control w-25", 'placeholder': 'Nome'}),
        }

        labels = {
            'name': "Nome",
        }


class AddAuthor(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'firstName': forms.TextInput(attrs={'class': "form-control w-25", 'placeholder': 'Nome'}),
            'lastName': forms.TextInput(attrs={'class': "form-control w-25", 'placeholder': 'Último Nome'}),
            'birthDate': forms.TextInput(attrs={'class': "form-control w-25", 'placeholder': 'Data de Nascimento'})
        }

        labels = {
            'firstName': "Primeiro Nome",
            'lastName': "Último Nome",
            'birthDate': "Data de Nascimento"
        }
