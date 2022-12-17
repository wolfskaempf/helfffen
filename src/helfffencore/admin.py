from django.contrib import admin

from .models import HelpOffer, Task


@admin.register(HelpOffer)
class HelpOfferAdmin(admin.ModelAdmin):
    list_filter = ('task',)
    search_fields = ['name', 'task__title']
    list_display = ('name', 'task', 'contact')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_of_helpers_needed', 'deadline', 'contact')
