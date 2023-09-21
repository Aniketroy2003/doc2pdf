from django.http import HttpResponse
from django.shortcuts import render
from .forms import DocumentForm
from .models import Document
import os
from docx2pdf import convert
import time
import pythoncom  # Import pythoncom

def convert_doc_to_pdf(docx_path):
    pdf_path = os.path.splitext(docx_path)[0] + ".pdf"
    convert(docx_path, pdf_path)
    return pdf_path

def convert_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()

            # Initialize COM before performing the conversion
            pythoncom.CoInitialize()

            pdf_path = convert_doc_to_pdf(document.doc_file.path)
            # time.sleep(1)
            with open(pdf_path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_path)}"'
                return response
    else:
        form = DocumentForm()
    return render(request, 'convert_document.html', {'form': form})
