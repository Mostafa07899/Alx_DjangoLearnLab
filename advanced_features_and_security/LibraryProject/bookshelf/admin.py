from django.contrib import admin
from .models import Book
from .models import CustomeUser
from django.contrib.auth.admin import UserAdmin 

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display fields in list view
    search_fields = ('title', 'author')  # Enable search
    list_filter = ('publication_year',)  # Enable filtering

admin.site.register(Book, BookAdmin)



class CustomUserAdmin(UserAdmin):
    model = CustomeUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomeUser, CustomUserAdmin)
