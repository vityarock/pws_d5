from django.contrib import admin

from p_library.models import Author, Book, Publisher, Reader


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = (
        'title',
        'author_full_name',
        'reader',
    )
    fields = (
        'ISBN',
        'title',
        'description',
        'year_release',
        'author',
        'price',
        'copy_count',
        'publisher',
        'reader',
    )



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    pass
