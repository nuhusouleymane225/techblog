from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'bases/home_base.html')

def author(request):
    return render(request, 'bases/tech-author.html')

def category01(request):
    return render(request, 'bases/tech-category-01.html')


def category02(request):
    return render(request, 'bases/tech-category-02.html')

def category03(request):
    return render(request, 'bases/tech-category-03.html')

def contact(request):
    return render(request, 'bases/tech-contact.html')

def single(request):
    return render(request, 'bases/tech-single.html')




