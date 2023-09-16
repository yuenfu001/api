from django.contrib import admin
from .models import Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id","first_name","middle_name","last_name"]
admin.site.register(Person,PersonAdmin)