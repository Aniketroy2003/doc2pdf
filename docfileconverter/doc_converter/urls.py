# doc_converter/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_document, name='convert_document'),
]
