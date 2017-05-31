from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_view(request):
    return HttpResponse('뭐라할까')

def main_view2(request):
    return HttpResponse('여기는 POST존입니다.')