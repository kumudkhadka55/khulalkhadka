from django.shortcuts import render

#User Home
def index(request):
    return render(request, 'index.html')