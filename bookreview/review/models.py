from django.db import models

# Create your models here.
class Book(models.Model):
    GENRE_CHOICES={
        'fiction':'Fiction',
        'non-fiction':'Non-Fiction',
        'sci-fi':'Sci-Fi',
        'history':'History',
        'romance':'Romance',
        'thriller':'Thriller',
        'comedy':'Comedy',
    }
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    description=models.TextField()
    genre=models.CharField(max_length=75,choices=GENRE_CHOICES)
    IBSN=models.DecimalField(max_digits=13,decimal_places=0)
    publication_date=models.DateField()
    average_rating=models.PositiveIntegerField()
