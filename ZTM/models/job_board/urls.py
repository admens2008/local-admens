from django.contrib import admin
from django.urls import path
from . views import index, job_detail

urlpatterns = [
    path('', index),
	path('job/<id>', job_detail, name='job-detail'),  
]