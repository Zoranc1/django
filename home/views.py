from django.shortcuts import render, HttpResponse
from .models import Book, Topic
# Create your views here.

def say_hello(request):
    
    topics = Topic.objects.all()
    
    if 'id' in request.GET:
        topic_id = request.GET['id']
        books = Book.objects.filter(topic=topic_id)
        
    else:
        books = Book.objects.all()
        
    return render(request,'home/index.html', {'books':books,'topics':topics})
    
    
    