from django.shortcuts import render
from .models import *
#from .train import myFun
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

import ast
from store.Img_Search.search import getSimilarImages
from .forms import PhotoUploadForm 
from pathlib import Path

directory = Path('C:\\Users\\hp\\Desktop\\ecom - Copy\\project\\media\\photos')


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_path = directory.iterdir()
            img_path= list(img_path)
            similar = getSimilarImages(img_path[-1])
            

            
            return render(request, 'store/upload_success.html',{'imgDic':list(similar.values())})
    else:
        form = PhotoUploadForm()
    return render(request, 'store/upload_photo.html', {'form': form})


@csrf_exempt
def imgSerachApi(request):
       if request.method == 'POST':
        # Access the picture data from the request
        picture = request.FILES.get('picture')

        # Process the picture as needed
        similar = getSimilarImages(picture)
        similar = list(similar.values())

        # Return a JSON response with the results
        response_data = {
            'result': similar[1:len(similar)],
           
        }
        return JsonResponse(response_data)

        # Handle other request methods or invalid requests
       return JsonResponse({'error': 'Invalid request'})  
     


