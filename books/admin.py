from django.contrib import admin

from books import models


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = models.Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "price",)


admin.site.register(models.Book, BookAdmin)
