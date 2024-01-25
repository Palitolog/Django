from django.shortcuts import render

def index(request):
    return render('../templates/index.html')
