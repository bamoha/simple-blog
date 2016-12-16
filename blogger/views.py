from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def index(request):
    return render(request, 'blogger/index.html')

def about(request):
    return render(request, 'blogger/about.html')

def post(request,pk):
    allPost = get_object_or_404(Post, pk=pk)
    context = {
        'allPost':allPost,
    }
    return render(request, 'blogger/post.html', context)

def contact(request):
    return render(request, 'blogger/contact.html')



