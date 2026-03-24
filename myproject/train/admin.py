from django.contrib import admin
from .models import Train, Carriage, TrainUnit

class TrainUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'previous_unit', 'next_unit')
    list_filter = ('name',)
    search_fields = ('name', 'number')
    readonly_fields = ('id',)

class TrainAdmin(TrainUnitAdmin):
    list_display = ('name', 'number', 'departure', 'arrival', 'departure_time', 'arrival_time')
    fieldsets = (
        ('Основна інформація', {'fields': ('name', 'number', 'id')}),
        ('Маршрут', {'fields': ('departure', 'arrival', 'departure_time', 'arrival_time')}),
        ('Додатково', {'fields': ('image', 'previous_unit', 'next_unit')}),
    )

class CarriageAdmin(TrainUnitAdmin):
    list_display = ("name", "number", "previous_unit", "next_unit", "image")
    fieldsets = (
        ('Основна інформація', {'fields': ('name', 'number', 'id')}),
        ('Додатково', {'fields': ('image', 'previous_unit', 'next_unit')}),
    )
    

admin.site.register(TrainUnit, TrainUnitAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(Carriage, CarriageAdmin)