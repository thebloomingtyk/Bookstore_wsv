from django.contrib import admin

from books import models


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price",)


admin.site.register(models.Book)
