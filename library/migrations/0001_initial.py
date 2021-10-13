# Generated by Django 3.2.8 on 2021-10-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('edition', models.CharField(max_length=50)),
                ('publication_year', models.IntegerField()),
                ('authors', models.ManyToManyField(related_name='books', to='library.Author')),
            ],
        ),
    ]
