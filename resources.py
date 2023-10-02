from import_export import resources
from table.models import MyTable


class TableResources(resources.ModelResource):
    class Meta:
        model = MyTable
