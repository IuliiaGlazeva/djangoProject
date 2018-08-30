from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Phone number for your questions: ', '(068)068-68-68', 'example@gmail.com']})
