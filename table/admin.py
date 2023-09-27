from django.contrib import admin
from .models import Department, MyTable


# Register the Department model with the admin site
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Register the MyTable model with the admin site
@admin.register(MyTable)
class MyTableAdmin(admin.ModelAdmin):
    list_display = ('department', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10')
    list_filter = ('department',)
    search_fields = ('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10')
