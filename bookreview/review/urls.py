from django.urls import path
from review import views
urlpatterns=[
    path('', views.home,name='home'),
    path('add/',views.addbook,name='addbook'),
    path('book/<int:book_id>/',views.details,name='details'),
]

