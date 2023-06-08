import random, json, requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return render(request, 'home.html')

@csrf_exempt
def login(request):
    return render(request, 'navbar/login.html')

@csrf_exempt
def cart(request):
    return render(request, 'navbar/cart.html')

@csrf_exempt
def about(request):
    return render(request, 'navbar/about.html')

@csrf_exempt
def privacy(request):
    return render(request, 'navbar/privacy.html')

@csrf_exempt
def contact(request):
    return render(request, 'navbar/contact.html')
