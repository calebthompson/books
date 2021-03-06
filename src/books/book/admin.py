from books.book.models import Book, Author, ISBN, Tag, Genre, Suggestion, Review, Rating
from django.contrib import admin
    
class ISBNInline(admin.TabularInline):
    model = ISBN
    extra = 1

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['title', 'author', 'publisher', 'description', 'language', 'publishYear']}),
                 ('Categories', {'fields' : ['tags', 'genres']}),
                 ('Reference Information', {'fields' : ['deweyDecimal']}),
                 ('External', {'fields': ['amazonURL', 'gutenbergURL', 'googleBooksURL', 'abeBooksURL']}),
                ]
    inlines = [ISBNInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(ISBN)
admin.site.register(Tag)
admin.site.register(Genre)
admin.site.register(Suggestion)
admin.site.register(Review)
admin.site.register(Rating)