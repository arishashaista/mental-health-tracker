from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152140',
        'name': 'Arisha Shaista Aurelya',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)