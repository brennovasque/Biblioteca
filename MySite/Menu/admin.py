from django.contrib import admin

from .models import Author, Book, Genre


class BookAdmin(admin.ModelAdmin):
    list_display = ('nome', 'genero', 'autor')

    @admin.display(description="Nome")
    def nome(self, obj):
        return obj.name

    @admin.display(description="Gênero")
    def genero(self, obj):
        return obj.genre

    @admin.display(description="Autor")
    def autor(self, obj):
        return obj.author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nome', )

    @admin.display(description="Nome Completo")
    def nome(self, obj):
        return obj


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genero', )

    @admin.display(description="Gênero")
    def genero(self, obj):
        return obj


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
