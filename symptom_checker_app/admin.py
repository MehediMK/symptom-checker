from django.contrib import admin
from .models import Patient, Symptom, Disease, Doctor


# Register your models here.
admin.site.register(Patient)
admin.site.register(Symptom)
admin.site.register(Disease)
admin.site.register(Doctor)


# @admin.register(Doctor)
# class DoctorAdmin(admin.ModelAdmin):
#     list_display=['id', 'name', 'specialty']
#     search_fields=['name', 'specialty']
