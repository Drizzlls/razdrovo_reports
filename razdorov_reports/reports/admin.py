from django.contrib import admin

from .models import Managers


class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'id_personal']

admin.site.register(Managers)