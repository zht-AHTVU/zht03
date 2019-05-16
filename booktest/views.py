from django.shortcuts import render,redirect
from booktest.models import BookInfo, AreaInfo
from datetime import date

# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books':books})

def create(request):
    '''新增一本图书'''
    book = BookInfo()
    book.book_name = '流星蝴蝶剑'
    book.book_pub_date = date(1990,1,1)
    book.save()
    return redirect('/index')

def delete(request,book_id):
    book = BookInfo.objects.get(id=book_id)
    book.delete()
    return redirect('/index')

def areas(request):
    area = AreaInfo.objects.get(area_name='广州市')
    #area_sons = AreaInfo.objects.filter(area_parent=area)
    area_sons = area.areainfo_set.all()
    return render(request,'booktest/area.html',{'area':area,'area_sons':area_sons})
