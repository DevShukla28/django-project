from django.shortcuts import render
from BRMApp.forms import NewBookForm ,Searchform
from BRMApp import models
from django.http import HttpResponse,HttpResponseRedirect

def searchBook(request):
     form=Searchform()
     res=render(request,'BRMApp/search_book.html',{'form':form})
     return res
def search(request):
        form=Searchform(request.POST)
        books=models.Book.objects.filter(title=form.data['title'])
        res=render(request,'BRMApp/search_book.html',{'form':form,'books':books})
        return res
def deletebook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRMApp/view_Books')
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRMApp/edit_book.html',{'form':form,'book':book})
    return res
def edit(request):
    if request.method=='POST':
         form=NewBookForm(request.POST)
         book=models.Book()
         bookid=request.POST['bookid']
         book.title=form.data['title']
         book.price=form.data['price']
         book.author=form.data['author']
         book.publisher=form.data['publisher']
         book.save()
    return HttpResponseRedirect('BRMApp/view_book')
def viewBooks(request):
    books=models.Book.objects.all()
    res= render(request,'BRMApp/view_book.html',{'books':books,})
    return res
def newbook(request):
    form=NewBookForm()
    res=render(request,'BRMApp/new_book.html',{'form':form})
    return res
def add(request):
    if request.method== 'POST':
        form= NewBookForm(request.POST)
        book= models.Book()
        book.title=form.data['title']
        book.price= form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
        s="Record Stored<br><a href='/BRMApp/view_book'>View all Books</a>"
        return HttpResponse(s)
