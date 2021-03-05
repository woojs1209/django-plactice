from django.contrib import admin
from . import models

@admin.register(models.Converstations)
class ConverstationsAdmin(admin.ModelAdmin):

    """ Converstations Admin Definition """

    pass
