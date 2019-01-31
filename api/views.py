from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from api.decorator.response import JsonResponseDecorator
import json
import base64
from api.utilities import temp2


# Create your views here.

@method_decorator(JsonResponseDecorator, name='dispatch')
class DataUpdateView(View):
    def post(self, request):
        # I will receive a JSON of a byte object here
        image = request.POST.get('image_string')
        image = base64.b64decode(image)
        print(image)
        x = temp2.func(image)
        print("Hi from line 21, views.py", x)
        return x
