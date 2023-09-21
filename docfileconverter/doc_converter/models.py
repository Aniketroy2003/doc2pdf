# doc_converter/models.py

from django.db import models

class Document(models.Model):
    doc_file = models.FileField(upload_to='documents/')
