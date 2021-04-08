from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(empdata)
class scannerex(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['name','department','rollno']

    class Meta:
        model=empdata
        fields=['id','Name','dept','rollno']
