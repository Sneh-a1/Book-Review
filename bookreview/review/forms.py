from django import forms 
from review.models import Book
from django.forms import ModelForm

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','description','genre','IBSN','publication_date','average_rating']
        label={
            'title':'Title',
            'author':'Author',
            'description':'Description',
            'genre':'Genre',
            'publication_date':'Publication Date',
            'average_rating':'Average Rating',

               }
        widgets={
            'publication_date':forms.DateInput(attrs={'placeholder':'yyyy-mm-dd'}),
        }
       
        



