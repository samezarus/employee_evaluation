from django.contrib import admin
from .models import *


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ["name", "parent", ]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "parent", "state", ]


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ["name", "alt_name", "city", ]


@admin.register(EmployeeGroup)
class EmployeeGroupAdmin(admin.ModelAdmin):
    list_display = ["name", "parent", ]


admin.site.register(Employee)
