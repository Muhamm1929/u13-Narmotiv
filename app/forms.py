from django import forms
from your_app_name.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"