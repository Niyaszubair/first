from django.shortcuts import render

# Create your views here.

# load first page
def load_first_page(request):
    return render(request,'first.html')

# load second page
def load_second_page(request):
    return render(request,'second.html')

# load index page
def load_index_page(request):
    return render(request,'index.html')