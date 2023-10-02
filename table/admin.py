from django.contrib import admin
from .models import Department, MyTable
from django.contrib.auth.models import User, Group
from import_export.admin import ImportExportModelAdmin
from resources import TableResources

admin.site.unregister(User)
admin.site.unregister(Group)


# Register the Department model with the admin site
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Register the MyTable model with the admin site
@admin.register(MyTable)
class MyTableAdmin(ImportExportModelAdmin):
    resource_classes = [TableResources]
    list_display = ('department', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10')
    list_filter = ('department',)
    search_fields = ('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10')
