from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class Author(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=20)
    birthDate = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['firstName']
        constraints = [
            UniqueConstraint(
                Lower('firstName'),
                Lower('lastName'),
                name='full_name',
                violation_error_message='Este autor já está cadastrado no sistema. Por favor, cadastre outro.'
            )
        ]

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Genre(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='name',
                violation_error_message='Este Gênero já está cadastrado no sistema. Por favor, cadastre outro.'
            )
        ]

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    name = models.CharField(max_length=40)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    amountPages = models.PositiveIntegerField()
    publicationDate = models.DateField()
    rent = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
