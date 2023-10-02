from django.shortcuts import render, redirect
from .models import Department, MyTable
from .forms import MyTableForm
from django.http import HttpResponse
from django.template import loader
import pdfkit


def list_departments(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})


def my_table_view(request):
    departments = Department.objects.all()
    selected_department_id = request.GET.get('department_id')

    if selected_department_id:
        selected_department = Department.objects.get(pk=selected_department_id)
        tables = MyTable.objects.filter(department=selected_department)
    else:
        tables = MyTable.objects.all()

    return render(request, 'table.html', {'departments': departments, 'tables': tables})

def generate_pdf(request):
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

    selected_department_id = request.GET.get('department_id')

    if selected_department_id:
        selected_department = Department.objects.get(pk=selected_department_id)
        table_data = MyTable.objects.filter(department=selected_department)
    else:
        table_data = MyTable.objects.all()

    template = loader.get_template('pdf_template.html')

    context = {
        'table': table_data,
    }

    html = template.render(context)

    pdf = pdfkit.from_string(html, False, configuration=config, options={'encoding': 'utf-8'})

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=table.pdf'

    return response



