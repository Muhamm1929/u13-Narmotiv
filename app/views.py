from django.shortcuts import render, redirect, get_object_or_404
from your_app_name.models import Book
from .forms import BookForm

# LIST
def book_list(request):
    books = Book.objects.all()
    return render(request, "books/list.html", {"books": books})

# CREATE
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("book_list")
    return render(request, "books/form.html", {"form": form})

# UPDATE
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("book_list")
    return render(request, "books/form.html", {"form": form})

# DELETE
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "books/delete.html", {"book": book})