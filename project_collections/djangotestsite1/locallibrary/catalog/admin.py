from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance,Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookInstance)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
  # inlines = [BooksInstanceInline]
   #pass
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #pass
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('genre','author')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    #pass
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('기본', {
            'fields': ('book', 'status','due_back')
        }),
       
    )

