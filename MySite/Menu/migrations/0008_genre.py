# Generated by Django 4.1.5 on 2023-01-04 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0007_delete_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]