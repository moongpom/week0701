from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:bookId>',detailPage,name="detailBook"),
    path('newBook/',newPage,name="newBook"),
    path('createBook/',create,name="createBook"),
    path('editBook/<str:bookId>',edit,name="editBook"),
    path('updateBook/<str:bookId>',update,name="updateBook"),
    path('deleteBook/<str:bookId>',delete,name="deleteBook"),
]