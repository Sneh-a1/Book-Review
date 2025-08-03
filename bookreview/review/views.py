from django.shortcuts import render,redirect
from review.models import Book
from review.forms import BookForm
from django.contrib import messages

# Create your views here.
def home(request):
    genre_selected=request.GET.get('genre')
    if genre_selected:
        books=Book.objects.filter(genre=genre_selected)
    else:    
        books=Book.objects.all()

    genres = Book.GENRE_CHOICES
    return render(request,'review/home.html',{
     'books':books,
     'genres':genres,
     'genre_selected':genre_selected,           
    })

def addbook(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added sucessfully !!")
            return redirect('home')
        else:
            messages.error(request, "Form submission incomplete. please check the details again !! ")
    else:
        form=BookForm()
    return render(request,'review/addbook.html',{'form':form})
                    

    
