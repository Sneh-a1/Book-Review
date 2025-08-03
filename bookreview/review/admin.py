from django.contrib import admin
from review.models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','genre','IBSN','publication_date','average_rating']
    




