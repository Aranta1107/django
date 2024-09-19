from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts =[
    {
       'author': 'Aranta Sinha',
       'title': 'Post 1',
       'content': 'My first post',
       'date_posted': '19 Sept , 2024'
    },
    {
       'author': 'Aditya Singh',
       'title': 'Post 2',
       'content': 'My first post',
       'date_posted': '19 Sept , 2024'
    }
]

def home(request):
	context ={
	   'posts':posts
	}
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html', {'title': 'About'})