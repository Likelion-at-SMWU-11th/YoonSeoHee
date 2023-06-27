from django.shortcuts import render

# Create your views here.

def studyLion(request):
    return render(request, 'funDjango.html')