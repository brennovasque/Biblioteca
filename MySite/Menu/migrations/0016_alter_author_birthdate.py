# Generated by Django 4.1.5 on 2023-01-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0015_alter_book_amountpages_alter_book_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]