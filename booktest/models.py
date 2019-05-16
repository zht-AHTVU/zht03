from django.db import models


# Create your models here.
class BookInfo(models.Model):
    book_name = models.CharField(max_length=20)
    book_pub_date = models.DateField()
    book_read = models.IntegerField(default=0)
    book_comment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

class HeroInfo(models.Model):
    hero_name = models.CharField(max_length=20)
    hero_gender = models.BooleanField(default=False)
    hero_comment = models.CharField(max_length=100)
    hero_book = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)


class AreaInfo(models.Model):
    area_name = models.CharField(max_length=20)
    area_parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)