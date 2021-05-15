from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Book
from .forms import BookForm
# Create your views here.
def homePage(request):
    books=Book.objects.all()
    return render(request,"homePage.html",{'bookContents':books})

def detailPage(request,bookId):
    books=get_object_or_404(Book,pk=bookId)
    return render(request,"detailPage.html",{'bookContents':books})

def newPage(request):
    form = BookForm()
    return render(request,'newPage.html',{'form':form})

def create(request):
    form = BookForm(request.POST,request.FILES)
    if form.is_valid():
        new_book = form.save(commit=False)
        new_book.new_date=timezone.now()
        new_book.save()
        return redirect("detailBook",new_book.id)
    return redirect('homePage') #﻿유효성 검사 실패 했을 땐 home으로 redirect할 수 있도록

def edit(request,bookId):
    editBook=Book.objects.get(id=bookId)
    return render(request,'editPage.html',{'bookContents':editBook})

def update(request,bookId):
    updateBook=Book.objects.get(id=bookId)
    updateBook.title=request.POST['title']
    updateBook.writer=request.POST['writer']
    updateBook.body=request.POST['body']
    updateBook.publisher=request.POST['publisher']
    updateBook.pub_date=request.POST['pub_date']
    updateBook.new_date=timezone.now()
    updateBook.save()
    return redirect("detailBook",updateBook.id)

def delete(request,bookId):
    deleteBook=Book.objects.get(id=bookId)
    deleteBook.delete()
    return redirect('homePage')

 