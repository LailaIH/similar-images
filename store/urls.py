from django.urls import path

from . import views

app_name ='store'

urlpatterns = [
	#Leave as empty string for base url

    path('photo/', views.upload_photo, name='upload_photo'),
    path('similar_image/', views.imgSerachApi, name='imgSerachApi'),
    
]