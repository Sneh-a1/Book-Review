from django.urls import path
from review import views
urlpatterns=[
    path('', views.home,name='home'),
    path('add/',views.addbook,name='addbook'),
]

