# Generated by Django 2.2.1 on 2019-05-08 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('book_pub_date', models.DateField()),
                ('book_read', models.IntegerField(default=0)),
                ('book_comment', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_name', models.CharField(max_length=20)),
                ('hero_gender', models.BooleanField(default=False)),
                ('hero_comment', models.CharField(max_length=100)),
                ('isDelete', models.BooleanField(default=False)),
                ('hero_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookInfo')),
            ],
        ),
    ]
