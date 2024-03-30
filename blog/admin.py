from django.contrib import admin
from . import models
from django.utils.text import slugify
# Register your models here.


class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',),}


admin.site.register(models.Categories, CategorieAdmin)
admin.site.register(models.Blog)
admin.site.register(models.Review)